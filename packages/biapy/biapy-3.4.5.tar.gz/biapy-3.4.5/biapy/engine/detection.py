import os
import math
import csv
import torch 
import torch.distributed as dist
import numpy as np
import pandas as pd
from skimage.feature import peak_local_max, blob_log
from skimage.measure import label, regionprops_table
from skimage.morphology import disk, dilation        
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

from biapy.data.data_2D_manipulation import load_and_prepare_2D_train_data
from biapy.data.data_3D_manipulation import load_and_prepare_3D_data
from biapy.data.post_processing.post_processing import (remove_close_points, detection_watershed, 
    measure_morphological_props_and_filter)
from biapy.data.pre_processing import create_detection_masks, norm_range01
from biapy.utils.util import save_tif, read_chunked_data, write_chunked_data, order_dimensions
from biapy.utils.misc import is_main_process, is_dist_avail_and_initialized
from biapy.engine.metrics import detection_metrics, jaccard_index, weighted_bce_dice_loss, CrossEntropyLoss_wrapper
from biapy.engine.base_workflow import Base_Workflow

class Detection_Workflow(Base_Workflow):
    """
    Detection workflow where the goal is to localize objects in the input image, not requiring a pixel-level class.
    More details in `our documentation <https://biapy.readthedocs.io/en/latest/workflows/detection.html>`_.  

    Parameters
    ----------
    cfg : YACS configuration
        Running configuration.
    
    Job_identifier : str
        Complete name of the running job.

    device : Torch device
        Device used. 

    args : argpase class
        Arguments used in BiaPy's call. 
    """
    def __init__(self, cfg, job_identifier, device, args, **kwargs):
        super(Detection_Workflow, self).__init__(cfg, job_identifier, device, args, **kwargs)

        # Detection stats
        self.stats['d_precision'] = 0
        self.stats['d_recall'] = 0
        self.stats['d_F1'] = 0
        self.stats['d_TP'] = 0
        self.stats['d_FP'] = 0
        self.stats['d_FN'] = 0

        self.stats['d_precision_merge_patches'] = 0
        self.stats['d_recall_merge_patches'] = 0
        self.stats['d_F1_merge_patches'] = 0
        self.stats['d_TP_merge_patches'] = 0
        self.stats['d_FP_merge_patches'] = 0
        self.stats['d_FN_merge_patches'] = 0

        self.original_test_mask_path = self.prepare_detection_data()

        self.use_gt = False 
        if self.cfg.DATA.TEST.LOAD_GT or self.cfg.DATA.TEST.USE_VAL_AS_TEST:
            self.use_gt = True 

        if self.use_gt:
            self.csv_files = sorted(next(os.walk(self.original_test_mask_path))[2])
        self.cell_count_file = os.path.join(self.cfg.PATHS.RESULT_DIR.PATH, 'cell_counter.csv')
        self.cell_count_lines = []

        # From now on, no modification of the cfg will be allowed
        self.cfg.freeze()

        # Activations for each output channel:
        # channel number : 'activation'
        self.activations = [{'0': 'CE_Sigmoid'}]

        # Workflow specific training variables
        self.mask_path = cfg.DATA.TRAIN.GT_PATH
        self.load_Y_val = True

        # Workflow specific test variables
        self.by_chunks = False
        if cfg.TEST.BY_CHUNKS.ENABLE and cfg.TEST.BY_CHUNKS.WORKFLOW_PROCESS.ENABLE and \
            cfg.TEST.BY_CHUNKS.WORKFLOW_PROCESS.TYPE == "chunk_by_chunk":
            self.by_chunks = True
            self.stats['d_precision_by_chunks'] = 0
            self.stats['d_recall_by_chunks'] = 0
            self.stats['d_F1_by_chunks'] = 0
            self.stats['d_TP_by_chunks'] = 0
            self.stats['d_FP_by_chunks'] = 0
            self.stats['d_FN_by_chunks'] = 0

        if self.cfg.TEST.POST_PROCESSING.DET_WATERSHED or self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS:
            self.post_processing['detection_post'] = True
        else:
            self.post_processing['detection_post'] = False    

        if self.cfg.PROBLEM.NDIM == '3D':
            self.v_size = (self.cfg.DATA.TEST.RESOLUTION[0], self.cfg.DATA.TEST.RESOLUTION[1], self.cfg.DATA.TEST.RESOLUTION[2])
        else:
            self.v_size = (1,self.cfg.DATA.TEST.RESOLUTION[0], self.cfg.DATA.TEST.RESOLUTION[1])
            
    def define_metrics(self):
        """
        Definition of self.metrics, self.metric_names and self.loss variables.
        """
        self.metrics = [
            jaccard_index(num_classes=self.cfg.MODEL.N_CLASSES, device=self.device, 
                torchvision_models=True if self.cfg.MODEL.SOURCE == "torchvision" else False)
        ]
        self.metric_names = ["jaccard_index"]
        if self.cfg.LOSS.TYPE == "CE": 
            self.loss = CrossEntropyLoss_wrapper(num_classes=self.cfg.MODEL.N_CLASSES,
                torchvision_models=True if self.cfg.MODEL.SOURCE == "torchvision" else False)
        elif self.cfg.LOSS.TYPE == "W_CE_DICE":
            self.loss = weighted_bce_dice_loss(w_dice=0.66, w_bce=0.33)

    def metric_calculation(self, output, targets, metric_logger=None):
        """
        Execution of the metrics defined in :func:`~define_metrics` function. 

        Parameters
        ----------
        output : Torch Tensor
            Prediction of the model. 

        targets : Torch Tensor
            Ground truth to compare the prediction with. 

        metric_logger : MetricLogger, optional
            Class to be updated with the new metric(s) value(s) calculated. 
        
        Returns
        -------
        value : float
            Value of the metric for the given prediction. 
        """
        with torch.no_grad():
            train_iou = self.metrics[0](output, targets)
            train_iou = train_iou.item() if not torch.isnan(train_iou) else 0
            if metric_logger is not None:
                metric_logger.meters[self.metric_names[0]].update(train_iou)
            else:
                return train_iou

    def detection_process(self, pred, filenames, metric_names=[], patch_pos=None, verbose=False):
        """
        Detection workflow engine for test/inference. Process model's prediction to prepare detection output and 
        calculate metrics. 

        Parameters
        ----------
        pred : 4D Torch tensor
            Model predictions. E.g. ``(z, y, x, channels)`` for both 2D and 3D.
        
        filenames : List of str
            Predicted image's filenames.

        metric_names : List of str
            Metrics names.
        """
        assert pred.ndim == 4, "Prediction doesn't have 4 dim: {pred.shape}"

        file_ext = os.path.splitext(filenames[0])[1]
        ndim = 2 if self.cfg.PROBLEM.NDIM == "2D" else 3
        pred_shape = pred.shape
        if self.cfg.TEST.VERBOSE:
            print("Capturing the local maxima ")
        all_points = []
        all_classes = []
        for channel in range(pred.shape[-1]):
            if self.cfg.TEST.VERBOSE:
                print("Class {}".format(channel+1))
            if len(self.cfg.TEST.DET_MIN_TH_TO_BE_PEAK) == 1:
                min_th_peak = self.cfg.TEST.DET_MIN_TH_TO_BE_PEAK[0]
            else:
                min_th_peak = self.cfg.TEST.DET_MIN_TH_TO_BE_PEAK[channel]
            
            # Find points
            if self.cfg.TEST.DET_POINT_CREATION_FUNCTION == "peak_local_max":
                pred_coordinates = peak_local_max(pred[...,channel].astype(np.float32),
                    min_distance=self.cfg.TEST.DET_PEAK_LOCAL_MAX_MIN_DISTANCE, threshold_abs=min_th_peak,
                    exclude_border=self.cfg.TEST.DET_EXCLUDE_BORDER)
            else:
                pred_coordinates = blob_log(pred[...,channel]*255, min_sigma=self.cfg.TEST.DET_BLOB_LOG_MIN_SIGMA, 
                    max_sigma=self.cfg.TEST.DET_BLOB_LOG_MAX_SIGMA, num_sigma=self.cfg.TEST.DET_BLOB_LOG_NUM_SIGMA, 
                    threshold=min_th_peak, exclude_border=self.cfg.TEST.DET_EXCLUDE_BORDER)
                pred_coordinates = pred_coordinates[:,:3].astype(int) # Remove sigma

            # Remove close points per class as post-processing method
            if self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS and not self.by_chunks:
                if len(self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS) == 1:
                    radius = self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS[0]
                else:
                    radius = self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS[channel]

                pred_coordinates = remove_close_points(pred_coordinates, radius, self.cfg.DATA.TEST.RESOLUTION,
                    ndim=ndim)
                    
            all_points.append(pred_coordinates)   
            c_size = 1 if len(pred_coordinates) == 0 else len(pred_coordinates)
            all_classes.append(np.full(c_size, channel))

        # Remove close points again seeing all classes together, as it can be that a point is detected in both classes
        # if there is not clear distinction between them
        classes = 1 if self.cfg.MODEL.N_CLASSES <= 2 else self.cfg.MODEL.N_CLASSES
        if self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS and classes > 1 and not self.by_chunks:
            if self.cfg.TEST.VERBOSE:
                print("All classes together")
            radius = np.min(self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS)

            all_points = np.concatenate(all_points, axis=0)
            all_classes = np.concatenate(all_classes, axis=0)

            new_points, all_classes = remove_close_points(all_points, radius, self.cfg.DATA.TEST.RESOLUTION,
                classes=all_classes, ndim=ndim)
            
            # Create again list of arrays of all points
            all_points = []
            for i in range(classes):
                all_points.append([])
            for i, c in enumerate(all_classes):
                all_points[c].append(new_points[i])
            del new_points

        # Create a file with detected point and other image with predictions ids (if GT given)
        if not self.by_chunks:
            if self.cfg.TEST.VERBOSE:
                print("Creating the images with detected points . . .")   
            points_pred = np.zeros(pred.shape[:-1], dtype=np.uint8)
            for n, pred_coordinates in enumerate(all_points):
                if self.use_gt:
                    pred_id_img = np.zeros(pred_shape[:-1], dtype=np.uint32)
                for j, coord in enumerate(pred_coordinates):
                    z,y,x = coord
                    points_pred[z,y,x] = n+1
                    if self.use_gt:
                        pred_id_img[z,y,x] = j+1
                
                # Dilate and save the prediction ids for the current class 
                if self.use_gt:
                    for i in range(pred_id_img.shape[0]):                                                                                  
                        pred_id_img[i] = dilation(pred_id_img[i], disk(3))
                    if file_ext in ['.hdf5', '.h5', ".zarr"]:
                        write_chunked_data(np.expand_dims(np.expand_dims(pred_id_img,-1),0), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, 
                            os.path.splitext(filenames[0])[0]+'_class'+str(n+1)+'_pred_ids'+file_ext, dtype_str="uint32", 
                            verbose=self.cfg.TEST.VERBOSE)
                    else:
                        save_tif(np.expand_dims(np.expand_dims(pred_id_img,0),-1), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS,
                            [os.path.splitext(filenames[0])[0]+'_class'+str(n+1)+'_pred_ids.tif'], verbose=self.cfg.TEST.VERBOSE)

                self.cell_count_lines.append([filenames, len(pred_coordinates)])

            if self.use_gt: del pred_id_img

            # Dilate and save the detected point image
            if len(pred_coordinates) > 0:
                for i in range(points_pred.shape[0]):                                                                                  
                    points_pred[i] = dilation(points_pred[i], disk(3)) 
            if file_ext in ['.hdf5', '.h5', ".zarr"]:
                write_chunked_data(np.expand_dims(np.expand_dims(points_pred,-1),0), self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK, 
                    filenames[0], dtype_str="uint8", verbose=self.cfg.TEST.VERBOSE)
            else:
                save_tif(np.expand_dims(np.expand_dims(points_pred,0),-1), self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK,
                    filenames, verbose=self.cfg.TEST.VERBOSE)

            # Detection watershed
            if self.cfg.TEST.POST_PROCESSING.DET_WATERSHED:
                data_filename = os.path.join(self.cfg.DATA.TEST.PATH, filenames[0])
                w_dir = os.path.join(self.cfg.PATHS.WATERSHED_DIR, filenames[0])
                check_wa = w_dir if self.cfg.PROBLEM.DETECTION.DATA_CHECK_MW else None
                points_pred = detection_watershed(points_pred, all_points, data_filename, self.cfg.TEST.POST_PROCESSING.DET_WATERSHED_FIRST_DILATION,
                    nclasses=classes, ndim=ndim, donuts_classes=self.cfg.TEST.POST_PROCESSING.DET_WATERSHED_DONUTS_CLASSES,
                    donuts_patch=self.cfg.TEST.POST_PROCESSING.DET_WATERSHED_DONUTS_PATCH, 
                    donuts_nucleus_diameter=self.cfg.TEST.POST_PROCESSING.DET_WATERSHED_DONUTS_NUCLEUS_DIAMETER, save_dir=check_wa)
                
                # Instance filtering by properties     
                points_pred, d_result = measure_morphological_props_and_filter(points_pred, self.cfg.DATA.TEST.RESOLUTION, 
                    properties=self.cfg.TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.PROPS, 
                    prop_values=self.cfg.TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.VALUES, 
                    comp_signs=self.cfg.TEST.POST_PROCESSING.MEASURE_PROPERTIES.REMOVE_BY_PROPERTIES.SIGN)

                if file_ext in ['.hdf5', '.h5', ".zarr"]:
                    write_chunked_data(np.expand_dims(np.expand_dims(points_pred,-1),0), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, 
                        filenames[0], dtype_str="uint8", verbose=self.cfg.TEST.VERBOSE)
                else:
                    save_tif(np.expand_dims(np.expand_dims(points_pred,0),-1), self.cfg.PATHS.RESULT_DIR.PER_IMAGE_POST_PROCESSING,
                        filenames, verbose=self.cfg.TEST.VERBOSE)
            del points_pred

        # Save coords in a couple of csv files            
        aux = np.concatenate(all_points, axis=0)
        df = None
        if len(aux) != 0:
            if self.cfg.PROBLEM.NDIM == "3D":
                prob = pred[aux[:,0], aux[:,1], aux[:,2], all_classes]
                prob = np.concatenate(prob, axis=0)
                all_classes = np.concatenate(all_classes, axis=0)
                if self.cfg.TEST.POST_PROCESSING.DET_WATERSHED:
                    df = pd.DataFrame(zip(d_result['labels'], list(aux[:,0]), list(aux[:,1]), list(aux[:,2]), list(prob), list(all_classes),
                        d_result['npixels'], d_result['areas'], d_result['sphericities'], d_result['diameters'], d_result['perimeters'], 
                        d_result['comment'], d_result['conditions']), columns =['pred_id', 'axis-0', 'axis-1', 'axis-2', 'probability', 
                        'class', 'npixels', 'volume', 'sphericity', 'diameter', 'perimeter (surface area)', 'comment', 'conditions'])
                    df = df.sort_values(by=['pred_id'])   
                else:
                    labels = []
                    for i, pred_coordinates in enumerate(all_points):
                        for j in range(len(pred_coordinates)):
                            labels.append(j+1)

                    df = pd.DataFrame(zip(labels, list(aux[:,0]), list(aux[:,1]), list(aux[:,2]), list(prob), list(all_classes)), 
                        columns =['pred_id', 'axis-0', 'axis-1', 'axis-2', 'probability', 'class'])
                    df = df.sort_values(by=['pred_id'])
            else:
                aux = aux[:,1:]
                prob = pred[0,aux[:,0], aux[:,1], all_classes]
                prob = np.concatenate(prob, axis=0)
                all_classes = np.concatenate(all_classes, axis=0)
                if self.cfg.TEST.POST_PROCESSING.DET_WATERSHED:
                    df = pd.DataFrame(zip(d_result['labels'], list(aux[:,0]), list(aux[:,1]), list(prob), list(all_classes),
                        d_result['npixels'], d_result['areas'], d_result['circularities'], d_result['diameters'], d_result['perimeters'], 
                        d_result['elongations'], d_result['comment'], d_result['conditions']), columns =['pred_id', 'axis-0', 'axis-1', 
                        'probability', 'class', 'npixels', 'area', 'circularity', 'diameter', 'perimeter', 'elongation', 'comment', 
                        'conditions'])
                    df = df.sort_values(by=['pred_id'])   
                else:
                    df = pd.DataFrame(zip(list(aux[:,0]), list(aux[:,1]), list(prob), list(all_classes)), 
                        columns =['axis-0', 'axis-1', 'probability', 'class'])
                    df = df.sort_values(by=['axis-0'])
            del aux 

            # Save just the points and their probabilities 
            os.makedirs(self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK, exist_ok=True)
            df.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK, os.path.splitext(filenames[0])[0]+'_full_info.csv'))
            if self.cfg.TEST.POST_PROCESSING.DET_WATERSHED:
                if ndim == 2:
                    cols = ['class', 'pred_id', 'npixels', 'area', 'circularity', 'perimeter', 'elongation', 'comment', 'conditions']
                else:
                    cols = ['class', 'pred_id', 'npixels', 'volume', 'sphericity', 'perimeter (surface area)', 'comment', 'conditions']
                df = df.drop(columns=cols)
            else:
                df = df.drop(columns=['class'])
            df.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK, os.path.splitext(filenames[0])[0]+'_prob.csv'))

        # Calculate detection metrics
        if self.use_gt:
            all_channel_d_metrics = [0,0,0,0,0,0]
            dfs = []
            gt_all_coords = []

            # Read the GT coordinates from the CSV file
            csv_filename = os.path.join(self.original_test_mask_path, os.path.splitext(filenames[0])[0]+'.csv')
            if not os.path.exists(csv_filename):
                if self.cfg.TEST.VERBOSE:
                    print("WARNING: The CSV file seems to have different name than image. Using the CSV file "
                            "with the same position as the CSV in the directory. Check if it is correct!")
                csv_filename = os.path.join(self.original_test_mask_path, self.csv_files[self.f_numbers[0]])
                if self.cfg.TEST.VERBOSE:
                    print("Its respective CSV file seems to be: {}".format(csv_filename))
            if self.cfg.TEST.VERBOSE:
                print("Reading GT data from: {}".format(csv_filename))
            df_gt = pd.read_csv(csv_filename, index_col=0)     
            df_gt = df_gt.rename(columns=lambda x: x.strip())
            zcoords = df_gt['axis-0'].tolist()
            ycoords = df_gt['axis-1'].tolist()
            class_info = None
            if self.cfg.PROBLEM.NDIM == '3D': 
                xcoords = df_gt['axis-2'].tolist()
                gt_coordinates = [[z,y,x] for z,y,x in zip(zcoords,ycoords,xcoords)]        
            else:
                gt_coordinates = [[0,y,x] for y,x in zip(zcoords,ycoords)]

            if len(df_gt.columns) == ndim+1:
                if 'class' not in df_gt:
                    raise ValueError(f"The column number {ndim+1}, if provided, must be 'class' (representing each point class)")
                else:
                    class_info = df_gt['class'].tolist()

            # Take only into account the GT points corresponding to the patch at hand 
            if patch_pos is not None:
                patch_gt_coordinates = []
                for j, cor in enumerate(gt_coordinates):
                    z,y,x = cor
                    z,y,x = int(z),int(y),int(x)
                    if patch_pos[0][0] <= z < patch_pos[0][1] and \
                        patch_pos[1][0] <= y < patch_pos[1][1] and \
                        patch_pos[2][0] <= x < patch_pos[2][1]:
                        z = z-patch_pos[0][0]
                        y = y-patch_pos[1][0]
                        x = x-patch_pos[2][0]
                        patch_gt_coordinates.append([z,y,x])
                        if z >= pred_shape[0] or y >= pred_shape[1] or x >= pred_shape[2]:
                            raise ValueError(f"Point [{z},{y},{x}] outside image with shape {pred_shape}")                           
                gt_coordinates = patch_gt_coordinates.copy()
            gt_all_coords.append(gt_coordinates)

            for ch, pred_coordinates in enumerate(all_points):
                # If there was class info take only the points related to the class at hand
                if class_info is not None:
                    class_points = []
                    for i in range(len(gt_coordinates)):
                        if int(class_info[i]) == ch:
                            class_points.append(gt_coordinates[i])
                    gt_coordinates = class_points.copy()
                    del class_points

                # Calculate detection metrics 
                if len(pred_coordinates) > 0:
                    if self.cfg.TEST.VERBOSE:
                        print("Detection (class "+str(ch+1)+")")
                    d_metrics, gt_assoc, fp = detection_metrics(gt_coordinates, pred_coordinates, tolerance=self.cfg.TEST.DET_TOLERANCE[ch],
                        voxel_size=self.v_size, return_assoc=True, verbose=self.cfg.TEST.VERBOSE)
                    if self.cfg.TEST.VERBOSE:
                        print("Detection metrics: {}".format(d_metrics))
                    all_channel_d_metrics[0] += d_metrics["Precision"]
                    all_channel_d_metrics[1] += d_metrics["Recall"]
                    all_channel_d_metrics[2] += d_metrics["F1"]
                    all_channel_d_metrics[3] += d_metrics["TP"]
                    all_channel_d_metrics[4] += d_metrics["FP"]
                    all_channel_d_metrics[5] += d_metrics["FN"]

                    # Save csv files with the associations between GT points and predicted ones
                    if gt_assoc is not None and fp is not None:
                        dfs.append([gt_assoc.copy(),fp.copy()])
                    else:
                        if gt_assoc is not None:
                            dfs.append([gt_assoc.copy(),None])
                        if fp is not None:
                            dfs.append([None, fp.copy()])
                    if self.cfg.PROBLEM.NDIM == "2D":
                        if gt_assoc is not None:
                            gt_assoc = gt_assoc.drop(columns=['axis-0'])
                            gt_assoc = gt_assoc.rename(columns={'axis-1': 'axis-0', 'axis-2': 'axis-1'})
                        if fp is not None:
                            fp = fp.drop(columns=['axis-0'])                    
                            fp = fp.rename(columns={'axis-1': 'axis-0', 'axis-2': 'axis-1'})
                    if gt_assoc is not None:
                        os.makedirs(self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, exist_ok=True)
                        gt_assoc.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, os.path.splitext(filenames[0])[0]+'_class'+str(ch+1)+'_gt_assoc.csv'))
                    if fp is not None:
                        os.makedirs(self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, exist_ok=True)
                        fp.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, os.path.splitext(filenames[0])[0]+'_class'+str(ch+1)+'_fp.csv'))             
                else:
                    if self.cfg.TEST.VERBOSE:
                        print("No point found to calculate the metrics!")

            if self.cfg.TEST.VERBOSE:
                if len(gt_coordinates) == 0: 
                    print("No points found in GT!")
                print("All classes "+str(ch+1))
            for k in range(len(all_channel_d_metrics)):
                all_channel_d_metrics[k] = all_channel_d_metrics[k]/len(all_points)
            if self.cfg.TEST.VERBOSE:
                print("Detection metrics: {}".format(["Precision", all_channel_d_metrics[0],
                    "Recall", all_channel_d_metrics[1], "F1", all_channel_d_metrics[2]]))

            if not self.by_chunks:
                self.stats[metric_names[0]] += all_channel_d_metrics[0]
                self.stats[metric_names[1]] += all_channel_d_metrics[1]
                self.stats[metric_names[2]] += all_channel_d_metrics[2]
                self.stats[metric_names[3]] += all_channel_d_metrics[3]
                self.stats[metric_names[4]] += all_channel_d_metrics[4]
                self.stats[metric_names[5]] += all_channel_d_metrics[5]

            if self.cfg.TEST.VERBOSE:
                print("Creating the image with a summary of detected points and false positives with colors . . .")
            if not self.by_chunks:
                points_pred = np.zeros(pred_shape[:-1]+(3,), dtype=np.uint8)
                for ch, gt_coords in enumerate(gt_all_coords):
                    # if gt_assoc is None: 
                    gt_assoc, fp = None, None
                    if len(dfs) > 0 and len(dfs[ch]) > 0:
                        if dfs[ch][0] is not None:
                            gt_assoc = dfs[ch][0]
                        if dfs[ch][1] is not None:
                            fp = dfs[ch][1]

                    # TP and FN
                    gt_id_img = np.zeros(pred_shape[:-1], dtype=np.uint32)
                    for j, cor in enumerate(gt_coords):
                        z,y,x = cor
                        z,y,x = int(z),int(y),int(x)
                        if gt_assoc is not None:
                            if gt_assoc[gt_assoc['gt_id'] == j+1]["tag"].iloc[0] == "TP":
                                points_pred[z,y,x] = (0,255,0)# Green
                            else:   
                                points_pred[z,y,x] = (255,0,0)# Red
                        else:                           
                            points_pred[z,y,x] = (255,0,0)# Red

                        gt_id_img[z,y,x] = j+1

                    # Dilate and save the GT ids for the current class 
                    for i in range(gt_id_img.shape[0]):      
                        gt_id_img[i] = dilation(gt_id_img[i], disk(3))
                    if file_ext in ['.hdf5', '.h5', ".zarr"]:
                        write_chunked_data(np.expand_dims(np.expand_dims(gt_id_img,-1),0), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, 
                            os.path.splitext(filenames[0])[0]+'_class'+str(ch+1)+'_gt_ids'+file_ext, dtype_str="uint32", 
                            verbose=self.cfg.TEST.VERBOSE)
                    else:
                        save_tif(np.expand_dims(np.expand_dims(gt_id_img,0),-1), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS,
                            [os.path.splitext(filenames[0])[0]+'_class'+str(ch+1)+'_gt_ids.csv'], verbose=self.cfg.TEST.VERBOSE)
                    
                    # FP
                    if fp is not None:
                        for cor in zip(fp['axis-0'].tolist(),fp['axis-1'].tolist(),fp['axis-2'].tolist()):
                            z, y, x =  cor  
                            z,y,x = int(z),int(y),int(x)
                            points_pred[z,y,x] = (0,0,255) # Blue

                # Dilate and save the predicted points for the current class 
                for i in range(points_pred.shape[0]):      
                    for j in range(points_pred.shape[-1]):                                                                              
                        points_pred[i,...,j] = dilation(points_pred[i,...,j], disk(3)) 
                if file_ext in ['.hdf5', '.h5', ".zarr"]:
                    write_chunked_data(np.expand_dims(points_pred,0), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS, filenames[0], 
                        dtype_str="uint8", verbose=self.cfg.TEST.VERBOSE)
                else:
                    save_tif(np.expand_dims(points_pred,0), self.cfg.PATHS.RESULT_DIR.DET_ASSOC_POINTS,
                        filenames, verbose=self.cfg.TEST.VERBOSE)    
                                
        return df 

    def normalize_stats(self, image_counter):
        """
        Normalize statistics.  

        Parameters
        ----------
        image_counter : int
            Number of images to average the metrics.
        """
        super().normalize_stats(image_counter)

        with open(self.cell_count_file, 'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['filename', 'cells'])
            for nr in range(len(self.cell_count_lines)):
                csvwriter.writerow([nr+1] + self.cell_count_lines[nr])
        if self.cfg.DATA.TEST.LOAD_GT or self.cfg.DATA.TEST.USE_VAL_AS_TEST:
            if self.by_chunks:
                self.stats['d_precision_by_chunks'] = self.stats['d_precision_by_chunks'] / image_counter
                self.stats['d_recall_by_chunks'] = self.stats['d_recall_by_chunks'] / image_counter
                self.stats['d_F1_by_chunks'] = self.stats['d_F1_by_chunks'] / image_counter
            else:
                if not self.cfg.TEST.FULL_IMG:
                    self.stats['d_precision_merge_patches'] = self.stats['d_precision_merge_patches'] / image_counter
                    self.stats['d_recall_merge_patches'] = self.stats['d_recall_merge_patches'] / image_counter
                    self.stats['d_F1_merge_patches'] = self.stats['d_F1_merge_patches'] / image_counter
                else:
                    self.stats['d_precision'] = self.stats['d_precision'] / image_counter
                    self.stats['d_recall'] = self.stats['d_recall'] / image_counter
                    self.stats['d_F1'] = self.stats['d_F1'] / image_counter

    def after_merge_patches(self, pred):
        """
        Steps need to be done after merging all predicted patches into the original image.

        Parameters
        ----------
        pred : Torch Tensor
            Model prediction.
        """
        if pred.shape[0] == 1:
            if self.cfg.PROBLEM.NDIM == "3D": pred = pred[0]
            self.detection_process(pred, self.processing_filenames, ['d_precision_merge_patches', 'd_recall_merge_patches', 
            'd_F1_merge_patches', 'd_TP_merge_patches', 'd_FP_merge_patches', 'd_FN_merge_patches'])
        else:
            NotImplementedError
        

    def process_patch(self, z, y, x, _filename, total_patches, c, pred, d, file_ext, z_dim, y_dim, x_dim):
        """
        Process a patch for the detection workflow.

        Parameters
        ----------
        z : int
            Patch z index.

        y : int
            Patch y index.

        x : int
            Patch x index.

        _filename : str
            Filename of the predicted image H5/Zarr.

        total_patches : int
            Total number of patches.

        c : int
            Current patch number.

        pred : 4D numpy array
            Model prediction.

        d : int
            Number of digits of the total patches.

        file_ext : str
            File extension of the predicted image.

        z_dim : int
            Dimension of the z axis.

        y_dim : int
            Dimension of the y axis.

        x_dim : int
            Dimension of the x axis.

        Returns
        -------
        df_patch : DataFrame
            Detected points in the patch.

        fname : str
            Filename of the patch.
        
        """
        print("Processing patch {}/{} of image".format(c, total_patches))
        if self.cfg.TEST.VERBOSE:    
            print("D: z: {}-{}, y: {}-{}, x: {}-{}".format(
                max(0,z*self.cfg.DATA.PATCH_SIZE[0]-self.cfg.DATA.TEST.PADDING[0]),min(z_dim,self.cfg.DATA.PATCH_SIZE[0]*(z+1)+self.cfg.DATA.TEST.PADDING[0]),
                max(0,y*self.cfg.DATA.PATCH_SIZE[1]-self.cfg.DATA.TEST.PADDING[1]),min(y_dim,self.cfg.DATA.PATCH_SIZE[1]*(y+1)+self.cfg.DATA.TEST.PADDING[1]),
                max(0,x*self.cfg.DATA.PATCH_SIZE[2]-self.cfg.DATA.TEST.PADDING[2]),min(x_dim,self.cfg.DATA.PATCH_SIZE[2]*(x+1)+self.cfg.DATA.TEST.PADDING[2])))
            
        fname = _filename+"_patch"+str(c).zfill(d)+file_ext
        
        slices = (
            slice(max(0,z*self.cfg.DATA.PATCH_SIZE[0]-self.cfg.DATA.TEST.PADDING[0]),min(z_dim,self.cfg.DATA.PATCH_SIZE[0]*(z+1)+self.cfg.DATA.TEST.PADDING[0])),
            slice(max(0,y*self.cfg.DATA.PATCH_SIZE[1]-self.cfg.DATA.TEST.PADDING[1]),min(y_dim,self.cfg.DATA.PATCH_SIZE[1]*(y+1)+self.cfg.DATA.TEST.PADDING[1])),
            slice(max(0,x*self.cfg.DATA.PATCH_SIZE[2]-self.cfg.DATA.TEST.PADDING[2]),min(x_dim,self.cfg.DATA.PATCH_SIZE[2]*(x+1)+self.cfg.DATA.TEST.PADDING[2])),
            slice(None), # Channel
        )
        
        data_ordered_slices = order_dimensions(
            slices,
            input_order = "ZYXC",
            output_order = self.cfg.TEST.BY_CHUNKS.INPUT_IMG_AXES_ORDER,
            default_value = 0,
            )

        raw_patch = pred[data_ordered_slices]

        if "C" not in self.cfg.TEST.BY_CHUNKS.INPUT_IMG_AXES_ORDER:                                                     
            expected_out_data_order = self.cfg.TEST.BY_CHUNKS.INPUT_IMG_AXES_ORDER + "C"                                
        else:                                                                                                           
            expected_out_data_order = self.cfg.TEST.BY_CHUNKS.INPUT_IMG_AXES_ORDER

        current_order = np.array(range(len(pred.shape)))
        transpose_order = order_dimensions(
                    current_order,
                    input_order= expected_out_data_order,
                    output_order= "ZYXC",
                    default_value= np.nan)

        transpose_order = [x for x in transpose_order if not np.isnan(x)]
        transpose_order = current_order[transpose_order]
        patch = raw_patch.transpose(transpose_order)

        patch_pos = [(k.start,k.stop) for k in slices]
        df_patch = self.detection_process(patch, [fname], patch_pos=patch_pos)
        
        if df_patch is not None: # if there is at least one point detected
            
            if z*self.cfg.DATA.PATCH_SIZE[0]-self.cfg.DATA.TEST.PADDING[0] >=0: # if a patch was added
                df_patch['axis-0'] = df_patch['axis-0'] - self.cfg.DATA.TEST.PADDING[0] # shift the coordinates to the correct patch position
            if y*self.cfg.DATA.PATCH_SIZE[1]-self.cfg.DATA.TEST.PADDING[1] >=0:
                df_patch['axis-1'] = df_patch['axis-1'] - self.cfg.DATA.TEST.PADDING[1]
            if x*self.cfg.DATA.PATCH_SIZE[2]-self.cfg.DATA.TEST.PADDING[2] >=0:
                df_patch['axis-2'] = df_patch['axis-2'] - self.cfg.DATA.TEST.PADDING[2]

            df_patch = df_patch[df_patch['axis-0'] >= 0] # remove all coordinate from the previous patch
            df_patch = df_patch[df_patch['axis-0'] < self.cfg.DATA.PATCH_SIZE[0]] # remove all coordinate from the next patch
            df_patch = df_patch[df_patch['axis-1'] >= 0]
            df_patch = df_patch[df_patch['axis-1'] < self.cfg.DATA.PATCH_SIZE[1]]
            df_patch = df_patch[df_patch['axis-2'] >= 0]
            df_patch = df_patch[df_patch['axis-2'] < self.cfg.DATA.PATCH_SIZE[2]]

            df_patch = df_patch.reset_index(drop=True)
            
            # add the patch shift to the detected coordinates
            shift = np.array([z*self.cfg.DATA.PATCH_SIZE[0], y*self.cfg.DATA.PATCH_SIZE[1], x*self.cfg.DATA.PATCH_SIZE[2]])
            df_patch['axis-0'] = df_patch['axis-0'] + shift[0]
            df_patch['axis-1'] = df_patch['axis-1'] + shift[1]
            df_patch['axis-2'] = df_patch['axis-2'] + shift[2]

            return df_patch, fname
        
        return None, None

    def after_merge_patches_by_chunks_proccess_patch(self, filename):
        """
        Place any code that needs to be done after merging all predicted patches into the original image
        but in the process made chunk by chunk. This function will operate patch by patch defined by
        ``DATA.PATCH_SIZE`` + ``DATA.PADDING``.

        Parameters
        ----------
        filename : List of str
            Filename of the predicted image H5/Zarr.
        """

        _filename, file_ext = os.path.splitext(os.path.basename(filename))
        print("Detection workflow pipeline continues for image {}".format(_filename))

        # Load H5/Zarr
        pred_file, pred = read_chunked_data(filename)

        t_dim, z_dim, c_dim, y_dim, x_dim = order_dimensions(pred.shape,
                        self.cfg.TEST.BY_CHUNKS.INPUT_IMG_AXES_ORDER)

        # Fill the new data
        z_vols = math.ceil(z_dim/self.cfg.DATA.PATCH_SIZE[0])
        y_vols = math.ceil(y_dim/self.cfg.DATA.PATCH_SIZE[1])
        x_vols = math.ceil(x_dim/self.cfg.DATA.PATCH_SIZE[2])
        total_patches = z_vols*y_vols*x_vols
        d = len(str(total_patches))
        c=1

        workers = self.cfg.SYSTEM.NUM_WORKERS if self.cfg.SYSTEM.NUM_WORKERS > 0 else None
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = []
            for z in tqdm(range(z_vols), disable=not is_main_process()):
                for y in range(y_vols):
                    for x in range(x_vols):
                        futures.append(executor.submit(self.process_patch, z, y, x, _filename, total_patches, c, pred, d, file_ext, z_dim, y_dim, x_dim))
                        c+=1
        df = None
        for future in futures:
            df_patch, fname = future.result()
            if df_patch is not None:
                if 'df' not in locals():
                    df = df_patch.copy()
                    df['file'] = fname
                else:
                    df_patch['file'] = fname
                    df = pd.concat([df, df_patch], ignore_index=True)

        # Take point coords
        pred_coordinates = []
        if df is None: 
            print("No points created, skipping evaluation . . .")
            return 
        coordz = df['axis-0'].tolist()
        coordy = df['axis-1'].tolist()
        coordx = df['axis-2'].tolist()
        for z,y,x in zip(coordz,coordy,coordx):
            pred_coordinates.append([z,y,x])

        # Apply post-processing of removing points
        if self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS and self.by_chunks:
            radius = self.cfg.TEST.POST_PROCESSING.REMOVE_CLOSE_POINTS_RADIUS[0]
            pred_coordinates, dropped_pos = remove_close_points(pred_coordinates, radius, self.cfg.DATA.TEST.RESOLUTION,
                ndim=3, return_drops=True)

            # Remove points from dataframe
            df = df.drop(dropped_pos)

        # Save large csv with all point of all patches
        df = df.sort_values(by=['file'])
        df.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.DET_LOCAL_MAX_COORDS_CHECK, _filename+'_all_points.csv'))

        if self.cfg.TEST.BY_CHUNKS.FORMAT == "h5":
            pred_file.close()

        # Calculate metrics with all the points  
        if self.use_gt:
            print("Calculating detection metrics with all the points found . . .")

            # Read the GT coordinates from the CSV file
            csv_filename = os.path.join(self.original_test_mask_path, os.path.splitext(filename[0])[0]+'.csv')
            if not os.path.exists(csv_filename):
                if self.cfg.TEST.VERBOSE:
                    print("WARNING: The CSV file seems to have different name than image. Using the CSV file "
                            "with the same position as the CSV in the directory. Check if it is correct!")
                csv_filename = os.path.join(self.original_test_mask_path, self.csv_files[self.f_numbers[0]])
                if self.cfg.TEST.VERBOSE:
                    print("Its respective CSV file seems to be: {}".format(csv_filename))
            if self.cfg.TEST.VERBOSE:
                print("Reading GT data from: {}".format(csv_filename))
            df_gt = pd.read_csv(csv_filename, index_col=0)   
            df_gt = df_gt.rename(columns=lambda x: x.strip())
            gt_coordinates = [[z,y,x] for z,y,x in zip(df_gt['axis-0'].tolist(),df_gt['axis-1'].tolist(),df_gt['axis-2'].tolist())]

            # Measure metrics
            d_metrics, gt_assoc, fp = detection_metrics(gt_coordinates, pred_coordinates, tolerance=self.cfg.TEST.DET_TOLERANCE[0],
                voxel_size=self.v_size, return_assoc=True, verbose=self.cfg.TEST.VERBOSE)
            print("Detection metrics: {}".format(d_metrics))

            self.stats['d_precision_by_chunks'] += d_metrics["Precision"]
            self.stats['d_recall_by_chunks'] += d_metrics["Recall"]
            self.stats['d_F1_by_chunks'] += d_metrics["F1"]
            self.stats['d_TP_by_chunks'] += d_metrics["TP"] 
            self.stats['d_FP_by_chunks'] += d_metrics["FP"] 
            self.stats['d_FN_by_chunks'] += d_metrics["FN"]

    def process_sample(self, norm):
        """
        Function to process a sample in the inference phase. 

        Parameters
        ----------
        norm : List of dicts
            Normalization used during training. Required to denormalize the predictions of the model.
        """
        if self.cfg.MODEL.SOURCE != "torchvision":
            super().process_sample(norm)
        else:
            # Data channel check
            if self.cfg.DATA.PATCH_SIZE[-1] != self._X.shape[-1]:
                raise ValueError("Channel of the DATA.PATCH_SIZE given {} does not correspond with the loaded image {}. "
                    "Please, check the channels of the images!".format(self.cfg.DATA.PATCH_SIZE[-1], self._X.shape[-1]))

            ##################
            ### FULL IMAGE ###
            ##################
            if self.cfg.TEST.FULL_IMG:
                # Make the prediction
                with torch.cuda.amp.autocast():
                    pred = self.model_call_func(self._X)
                del self._X 

    def torchvision_model_call(self, in_img, is_train=False):
        """
        Call a regular Pytorch model.

        Parameters
        ----------
        in_img : Tensor
            Input image to pass through the model.

        is_train : bool, optional
            Whether if the call is during training or inference. 

        Returns
        -------
        prediction : Tensor 
            Image prediction. 
        """
        filename, file_extension = os.path.splitext(self.processing_filenames[0])

        # Convert first to 0-255 range if uint16
        if in_img.dtype == torch.float32:
            if torch.max(in_img) > 1:
                in_img = (norm_range01(in_img, torch.uint8)[0]*255).to(torch.uint8)
            in_img = in_img.to(torch.uint8)
        
        # Apply TorchVision pre-processing
        in_img = self.torchvision_preprocessing(in_img)

        pred = self.model(in_img)

        bboxes = pred[0]['boxes'].cpu().numpy()
        if not is_train and len(bboxes) != 0:
            # Extract each output from prediction
            labels = pred[0]['labels'].cpu().numpy()
            scores = pred[0]['scores'].cpu().numpy()
            
            # Save all info in a csv file
            df = pd.DataFrame(zip(labels, scores, bboxes[:,0],bboxes[:,1],bboxes[:,2],bboxes[:,3]), 
                columns = ['label', 'scores', 'x1', 'y1', 'x2', 'y2'])
            df = df.sort_values(by=['label']) 
            df.to_csv(os.path.join(self.cfg.PATHS.RESULT_DIR.FULL_IMAGE, filename+".csv"), index=False)

        return None

    def after_full_image(self, pred):
        """
        Steps that must be executed after generating the prediction by supplying the entire image to the model.

        Parameters
        ----------
        pred : Torch Tensor
            Model prediction.
        """
        if pred.shape[0] == 1:
            if self.cfg.PROBLEM.NDIM == "3D": pred = pred[0]
            self.detection_process(pred, self.processing_filenames, ['d_precision', 'd_recall', 'd_F1', 'd_TP', 'd_FP', 'd_FN'])
        else:
            NotImplementedError
        

    def after_all_images(self):
        """
        Steps that must be done after predicting all images. 
        """
        super().after_all_images()

    def print_stats(self, image_counter):
        """
        Print statistics.  

        Parameters
        ----------
        image_counter : int
            Number of images to call ``normalize_stats``.
        """
        if not self.use_gt or self.cfg.MODEL.SOURCE == "torchvision": return 

        super().print_stats(image_counter)
        super().print_post_processing_stats()

        print("Detection specific metrics:")
        if self.cfg.DATA.TEST.LOAD_GT or self.cfg.DATA.TEST.USE_VAL_AS_TEST:
            if self.by_chunks:
                print("Detection - Test Precision (per image): {}".format(self.stats['d_precision_by_chunks']))
                print("Detection - Test Recall (per image): {}".format(self.stats['d_recall_by_chunks']))
                print("Detection - Test F1 (per image): {}".format(self.stats['d_F1_by_chunks']))
                print("Detection - Test TP (per image): {}".format(self.stats['d_TP_by_chunks']))
                print("Detection - Test FP (per image): {}".format(self.stats['d_FP_by_chunks']))
                print("Detection - Test FN (per image): {}".format(self.stats['d_FN_by_chunks']))
            else:
                if not self.cfg.TEST.FULL_IMG:
                    print("Detection - Test Precision (merge patches): {}".format(self.stats['d_precision_merge_patches']))
                    print("Detection - Test Recall (merge patches): {}".format(self.stats['d_recall_merge_patches']))
                    print("Detection - Test F1 (merge patches): {}".format(self.stats['d_F1_merge_patches']))
                    print("Detection - Test TP (merge patches): {}".format(self.stats['d_TP_merge_patches']))
                    print("Detection - Test FP (merge patches): {}".format(self.stats['d_FP_merge_patches']))
                    print("Detection - Test FN (merge patches): {}".format(self.stats['d_FN_merge_patches']))
                else:
                    print("Detection - Test Precision (per image): {}".format(self.stats['d_precision']))
                    print("Detection - Test Recall (per image): {}".format(self.stats['d_recall']))
                    print("Detection - Test F1 (per image): {}".format(self.stats['d_F1']))
                    print("Detection - Test TP (per image): {}".format(self.stats['d_TP']))
                    print("Detection - Test FP (per image): {}".format(self.stats['d_FP']))
                    print("Detection - Test FN (per image): {}".format(self.stats['d_FN']))

    def prepare_detection_data(self):
        """
        Creates detection ground truth images to train the model based on the ground truth coordinates provided.
        They will be saved in a separate folder in the root path of the ground truth. 
        """
        original_test_mask_path = None
        create_mask = False

        if is_main_process():
            print("############################")
            print("#  PREPARE DETECTION DATA  #")
            print("############################")

            # Create selected channels for train data
            if self.cfg.TRAIN.ENABLE or self.cfg.DATA.TEST.USE_VAL_AS_TEST:
                create_mask = False
                if not os.path.isdir(self.cfg.DATA.TRAIN.DETECTION_MASK_DIR):
                    print("You select to create detection masks from given .csv files but no file is detected in {}. "
                        "So let's prepare the data. Notice that, if you do not modify 'DATA.TRAIN.DETECTION_MASK_DIR' "
                        "path, this process will be done just once!".format(self.cfg.DATA.TRAIN.DETECTION_MASK_DIR))
                    create_mask = True
                else:
                    if len(next(os.walk(self.cfg.DATA.TRAIN.DETECTION_MASK_DIR))[2]) != len(next(os.walk(self.cfg.DATA.TRAIN.GT_PATH))[2]) and \
                       len(next(os.walk(self.cfg.DATA.TRAIN.DETECTION_MASK_DIR))[1]) != len(next(os.walk(self.cfg.DATA.TRAIN.GT_PATH))[2]):
                        print("Different number of files found in {} and {}. Trying to create the the rest again"
                            .format(self.cfg.DATA.TRAIN.GT_PATH,self.cfg.DATA.TRAIN.DETECTION_MASK_DIR))
                        create_mask = True    

                if create_mask:
                    create_detection_masks(self.cfg)

            # Create selected channels for val data
            if self.cfg.TRAIN.ENABLE and not self.cfg.DATA.VAL.FROM_TRAIN:
                create_mask = False
                if not os.path.isdir(self.cfg.DATA.VAL.DETECTION_MASK_DIR):
                    print("You select to create detection masks from given .csv files but no file is detected in {}. "
                        "So let's prepare the data. Notice that, if you do not modify 'DATA.VAL.DETECTION_MASK_DIR' "
                        "path, this process will be done just once!".format(self.cfg.DATA.VAL.DETECTION_MASK_DIR))
                    create_mask = True
                else:
                    if len(next(os.walk(self.cfg.DATA.VAL.DETECTION_MASK_DIR))[2]) != len(next(os.walk(self.cfg.DATA.VAL.GT_PATH))[2]) and \
                       len(next(os.walk(self.cfg.DATA.VAL.DETECTION_MASK_DIR))[1]) != len(next(os.walk(self.cfg.DATA.VAL.GT_PATH))[2]):
                        print("Different number of files found in {} and {}. Trying to create the the rest again"
                            .format(self.cfg.DATA.VAL.GT_PATH,self.cfg.DATA.VAL.DETECTION_MASK_DIR))
                        create_mask = True 
                        
                if create_mask:
                    create_detection_masks(self.cfg, data_type='val')

            # Create selected channels for test data once
            if self.cfg.TEST.ENABLE and self.cfg.DATA.TEST.LOAD_GT and not self.cfg.DATA.TEST.USE_VAL_AS_TEST:
                create_mask = False
                if not os.path.isdir(self.cfg.DATA.TEST.DETECTION_MASK_DIR):
                    print("You select to create detection masks from given .csv files but no file is detected in {}. "
                        "So let's prepare the data. Notice that, if you do not modify 'DATA.TEST.DETECTION_MASK_DIR' "
                        "path, this process will be done just once!".format(self.cfg.DATA.TEST.DETECTION_MASK_DIR))
                    create_mask = True
                else:
                    if len(next(os.walk(self.cfg.DATA.TEST.DETECTION_MASK_DIR))[2]) != len(next(os.walk(self.cfg.DATA.TEST.GT_PATH))[2]) and \
                       len(next(os.walk(self.cfg.DATA.TEST.DETECTION_MASK_DIR))[1]) != len(next(os.walk(self.cfg.DATA.TEST.GT_PATH))[2]):
                        print("Different number of files found in {} and {}. Trying to create the the rest again"
                            .format(self.cfg.DATA.TEST.GT_PATH,self.cfg.DATA.TEST.DETECTION_MASK_DIR))
                        create_mask = True 
                if create_mask:
                    create_detection_masks(self.cfg, data_type='test')

        if is_dist_avail_and_initialized():
            dist.barrier()

        opts = []
        if self.cfg.TRAIN.ENABLE:
            print("DATA.TRAIN.GT_PATH changed from {} to {}".format(self.cfg.DATA.TRAIN.GT_PATH, self.cfg.DATA.TRAIN.DETECTION_MASK_DIR))
            opts.extend(['DATA.TRAIN.GT_PATH', self.cfg.DATA.TRAIN.DETECTION_MASK_DIR])
            if not self.cfg.DATA.VAL.FROM_TRAIN:
                print("DATA.VAL.GT_PATH changed from {} to {}".format(self.cfg.DATA.VAL.GT_PATH, self.cfg.DATA.VAL.DETECTION_MASK_DIR))
                opts.extend(['DATA.VAL.GT_PATH', self.cfg.DATA.VAL.DETECTION_MASK_DIR])
            if create_mask and self.cfg.DATA.TRAIN.INPUT_MASK_AXES_ORDER != 'TZCYX':
                print(f"DATA.TRAIN.INPUT_MASK_AXES_ORDER changed from '{self.cfg.DATA.TRAIN.INPUT_MASK_AXES_ORDER}' to 'TZCYX'. Remember to set that value "
                    " in future runs if you reuse the mask created.")
                opts.extend(['DATA.TRAIN.INPUT_MASK_AXES_ORDER', 'TZCYX']) 
        if self.cfg.TEST.ENABLE and self.cfg.DATA.TEST.LOAD_GT:
            print("DATA.TEST.GT_PATH changed from {} to {}".format(self.cfg.DATA.TEST.GT_PATH, self.cfg.DATA.TEST.DETECTION_MASK_DIR))
            opts.extend(['DATA.TEST.GT_PATH', self.cfg.DATA.TEST.DETECTION_MASK_DIR])
            original_test_mask_path = self.cfg.DATA.TEST.GT_PATH
        self.cfg.merge_from_list(opts)
        

        return original_test_mask_path