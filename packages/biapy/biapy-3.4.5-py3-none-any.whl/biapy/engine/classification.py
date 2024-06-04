import os
import torch
import math
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from torchmetrics import Accuracy
from sklearn.model_selection import StratifiedKFold

from biapy.engine.base_workflow import Base_Workflow
from biapy.data.pre_processing import norm_range01
from biapy.data.data_2D_manipulation import load_data_classification
from biapy.data.data_3D_manipulation import load_3d_data_classification
from biapy.utils.misc import is_main_process
from biapy.data.pre_processing import preprocess_data

class Classification_Workflow(Base_Workflow):
    """
    Classification workflow where the goal of this workflow is to assing a label to the input image.
    More details in `our documentation <https://biapy.readthedocs.io/en/latest/workflows/classification.html>`_. 

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
        super(Classification_Workflow, self).__init__(cfg, job_identifier, device, args, **kwargs)
        self.stats['test_accuracy'] = 0
        self.stats['cm'] = None
        self.all_pred = [] 
        if self.cfg.DATA.TEST.LOAD_GT: 
            self.all_gt = []
        self.test_filenames = None
        self.class_names = None

        # From now on, no modification of the cfg will be allowed
        self.cfg.freeze()

        # Activations for each output channel:
        # channel number : 'activation'
        self.activations = [{':': 'Linear'}]

        # Workflow specific training variables
        self.mask_path = cfg.DATA.TRAIN.GT_PATH
        self.load_Y_val = True

    def define_metrics(self):
        """
        Definition of self.metrics, self.metric_names and self.loss variables.
        """
        self.metrics = [Accuracy(task="multiclass", num_classes=self.cfg.MODEL.N_CLASSES)]
        self.metric_names = ["accuracy"]
        if self.cfg.MODEL.N_CLASSES > 5:
            self.metrics.append(Accuracy(task="multiclass", num_classes=self.cfg.MODEL.N_CLASSES, top_k=5))
            self.metric_names.append("top-5-accuracy")
        self.loss = torch.nn.CrossEntropyLoss()

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
            train_acc = self.metrics[0](output.to(torch.float32).detach().cpu(), targets.to(torch.float32).detach().cpu())
            train_acc = train_acc.item() if not torch.isnan(train_acc) else 0
            if self.cfg.MODEL.N_CLASSES > 5:
                train_5acc = self.metrics[1](output.to(torch.float32).detach().cpu(), targets.to(torch.float32).detach().cpu())
                train_5acc = train_5acc.item() if not torch.isnan(train_5acc) else 0
            if metric_logger is not None:
                metric_logger.meters[self.metric_names[0]].update(train_acc)
                if self.cfg.MODEL.N_CLASSES > 5:
                    metric_logger.meters[self.metric_names[1]].update(train_5acc)
            else:
                return train_acc

    def prepare_targets(self, targets, batch):
        """
        Location to perform any necessary data transformations to ``targets``
        before calculating the loss.

        Parameters
        ----------
        targets : Torch Tensor
            Ground truth to compare the prediction with.

        batch : Torch Tensor
            Prediction of the model. Not used here.

        Returns
        -------
        targets : Torch tensor
            Resulting targets. 
        """
        return targets.to(self.device, non_blocking=True)

    def load_train_data(self):
        """ 
        Load training and validation data.
        """
        if self.cfg.TRAIN.ENABLE:
            print("##########################\n"
                  "#   LOAD TRAINING DATA   #\n"
                  "##########################\n")
            if self.cfg.DATA.TRAIN.IN_MEMORY:
                val_split = self.cfg.DATA.VAL.SPLIT_TRAIN if self.cfg.DATA.VAL.FROM_TRAIN else 0.
                f_name = load_data_classification if self.cfg.PROBLEM.NDIM == '2D' else load_3d_data_classification
                preprocess_cfg = self.cfg.DATA.PREPROCESS if self.cfg.DATA.PREPROCESS.TRAIN else None
                preprocess_fn = preprocess_data if self.cfg.DATA.PREPROCESS.TRAIN else None
                print("0) Loading train images . . .")
                objs = f_name(self.cfg.DATA.TRAIN.PATH, self.cfg.DATA.PATCH_SIZE, convert_to_rgb=self.cfg.DATA.FORCE_RGB,
                    expected_classes=self.cfg.MODEL.N_CLASSES, cross_val=self.cfg.DATA.VAL.CROSS_VAL, 
                    cross_val_nsplits=self.cfg.DATA.VAL.CROSS_VAL_NFOLD, cross_val_fold=self.cfg.DATA.VAL.CROSS_VAL_FOLD, 
                    val_split=val_split, seed=self.cfg.SYSTEM.SEED, shuffle_val=self.cfg.DATA.VAL.RANDOM, 
                    preprocess_cfg=preprocess_cfg, preprocess_f=preprocess_fn)
            
                if self.cfg.DATA.VAL.FROM_TRAIN:
                    if self.cfg.DATA.VAL.CROSS_VAL:
                        self.X_train, self.Y_train, self.X_val, self.Y_val, self.train_filenames, self.cross_val_samples_ids = objs
                    else:
                        self.X_train, self.Y_train, self.X_val, self.Y_val, self.train_filenames = objs
                else:
                    self.X_train, self.Y_train, self.train_filenames = objs
                del objs
            else:
                self.X_train, self.Y_train = None, None

            ##################
            ### VALIDATION ###
            ##################
            if not self.cfg.DATA.VAL.FROM_TRAIN:
                if self.cfg.DATA.VAL.IN_MEMORY:
                    print("1) Loading validation images . . .")
                    f_name = load_data_classification if self.cfg.PROBLEM.NDIM == '2D' else load_3d_data_classification
                    preprocess_cfg = self.cfg.DATA.PREPROCESS if self.cfg.DATA.PREPROCESS.VAL else None
                    preprocess_fn = preprocess_data if self.cfg.DATA.PREPROCESS.VAL else None
                    self.X_val, self.Y_val, _ = f_name(self.cfg.DATA.VAL.PATH, self.cfg.DATA.PATCH_SIZE, 
                        convert_to_rgb=self.cfg.DATA.FORCE_RGB, expected_classes=self.cfg.MODEL.N_CLASSES, 
                        val_split=0, preprocess_cfg=preprocess_cfg, preprocess_f=preprocess_fn)

                    if self.Y_val is not None and len(self.X_val) != len(self.Y_val):
                        raise ValueError("Different number of raw and ground truth items ({} vs {}). "
                            "Please check the data!".format(len(self.X_val), len(self.Y_val)))
                else:
                    self.X_val, self.Y_val = None, None

    def load_test_data(self):
        """
        Load test data.
        """
        if self.cfg.TEST.ENABLE:
            print("######################\n"
                  "#   LOAD TEST DATA   #\n"
                  "######################\n")
            if not self.cfg.DATA.TEST.USE_VAL_AS_TEST:
                if self.cfg.DATA.TEST.IN_MEMORY:
                    print("2) Loading test images . . .")
                    f_name = load_data_classification if self.cfg.PROBLEM.NDIM == '2D' else load_3d_data_classification
                    preprocess_cfg = self.cfg.DATA.PREPROCESS if self.cfg.DATA.PREPROCESS.TEST else None
                    preprocess_fn = preprocess_data if self.cfg.DATA.PREPROCESS.TEST else None
                    self.X_test, self.Y_test, self.test_filenames = f_name(self.cfg.DATA.TEST.PATH, self.cfg.DATA.PATCH_SIZE,
                        convert_to_rgb=self.cfg.DATA.FORCE_RGB, preprocess_cfg=preprocess_cfg, preprocess_f=preprocess_fn,
                        expected_classes=self.cfg.MODEL.N_CLASSES if self.cfg.DATA.TEST.LOAD_GT else None, val_split=0)
                    self.class_names = sorted(next(os.walk(self.cfg.DATA.TEST.PATH))[1])
                else:
                    self.X_test, self.Y_test = None, None

                self.class_names = sorted(next(os.walk(self.cfg.DATA.TEST.PATH))[1])
                if self.test_filenames is None:
                    self.test_filenames = []
                    for c_num, folder in enumerate(self.class_names):
                        self.test_filenames += sorted(next(os.walk(os.path.join(self.cfg.DATA.TEST.PATH, folder)))[2])
            else:
                # The test is the validation, and as it is only available when validation is obtained from train and when 
                # cross validation is enabled, the test set files reside in the train folder
                self.X_test, self.Y_test = None, None
                self.class_names = sorted(next(os.walk(self.cfg.DATA.TRAIN.PATH))[1])
                if self.cross_val_samples_ids is None:                      
                    # Split the test as it was the validation when train is not enabled 
                    skf = StratifiedKFold(n_splits=self.cfg.DATA.VAL.CROSS_VAL_NFOLD, shuffle=self.cfg.DATA.VAL.RANDOM,
                        random_state=self.cfg.SYSTEM.SEED)
                    fold = 1
                    test_index = None
                    self.test_filenames = []
                    B = []
                    for c_num, folder in enumerate(self.class_names):
                        ids = sorted(next(os.walk(os.path.join(self.cfg.DATA.TRAIN.PATH,folder)))[2])
                        B.append((c_num,)*len(ids))
                        self.test_filenames += ids
                    A = np.zeros(len(self.test_filenames)) 
                    B = np.concatenate(B, 0)  
                
                    for _, te_index in skf.split(A, B):
                        if self.cfg.DATA.VAL.CROSS_VAL_FOLD == fold:
                            self.cross_val_samples_ids = te_index.copy()
                            break
                        fold += 1
                    if len(self.cross_val_samples_ids) > 5:
                        print("Fold number {} used for test data. Printing the first 5 ids: {}".format(fold, self.cross_val_samples_ids[:5]))
                    else:
                        print("Fold number {}. Indexes used in cross validation: {}".format(fold, self.cross_val_samples_ids))
                
                if self.test_filenames is None:
                    self.test_filenames = []
                    for c_num, folder in enumerate(self.class_names):
                        f = os.path.join(self.cfg.DATA.TRAIN.PATH, folder)
                        ids = sorted(next(os.walk(f))[2])
                        self.test_filenames += ids
                self.test_filenames = [x for i, x in enumerate(self.test_filenames) if i in self.cross_val_samples_ids]
                self.original_test_path = self.orig_train_path
                self.original_test_mask_path = self.orig_train_mask_path  

    def process_sample(self, norm):   
        """
        Function to process a sample in the inference phase. 

        Parameters
        ----------
        norm : List of dicts
            Normalization used during training. Required to denormalize the predictions of the model.
        """
        # Predict each patch
        l = int(math.ceil(self._X.shape[0]/self.cfg.TRAIN.BATCH_SIZE))
        for k in tqdm(range(l), leave=False, disable=not is_main_process()):
            top = (k+1)*self.cfg.TRAIN.BATCH_SIZE if (k+1)*self.cfg.TRAIN.BATCH_SIZE < self._X.shape[0] else self._X.shape[0]
            with torch.cuda.amp.autocast():
                p = self.model_call_func(self._X[k*self.cfg.TRAIN.BATCH_SIZE:top]).cpu().numpy()
            p = np.argmax(p, axis=1)
            self.all_pred.append(p)
            self.stats['patch_by_batch_counter'] += 1 

        if self.cfg.DATA.TEST.LOAD_GT: 
            self.all_gt.append(self._Y)

    def torchvision_model_call(self, in_img, is_train=False):
        """
        Call a regular Pytorch model.

        Parameters
        ----------
        in_img : Tensors
            Input image to pass through the model.

        is_train : bool, optional
            Whether if the call is during training or inference. 

        Returns
        -------
        prediction : Tensor 
            Image prediction. 
        """
        # Convert first to 0-255 range if uint16
        if in_img.dtype == torch.float32:
            if torch.max(in_img) > 255:
                in_img = (norm_range01(in_img, torch.uint8)[0]*255).to(torch.uint8)
            in_img = in_img.to(torch.uint8)
    
        # Apply TorchVision pre-processing
        in_img = self.torchvision_preprocessing(in_img)

        return self.model(in_img)        

    def after_all_images(self):
        """
        Steps that must be done after predicting all images. 
        """
        # Save predictions in a csv file
        df = pd.DataFrame(self.test_filenames, columns=['filename'])
        df['class'] = np.array(self.all_pred).squeeze()
        f= os.path.join(self.cfg.PATHS.RESULT_DIR.PATH, "predictions.csv")
        os.makedirs(self.cfg.PATHS.RESULT_DIR.PATH, exist_ok=True)
        df.to_csv(f, index=False, header=True)

        if self.cfg.DATA.TEST.LOAD_GT and self.cfg.TEST.EVALUATE:
            self.stats['test_accuracy'] = accuracy_score(self.all_gt, self.all_pred)
            self.stats['cm'] = confusion_matrix(self.all_gt, self.all_pred)
    
    def print_stats(self, image_counter):
        """
        Print statistics.  

        Parameters
        ----------
        image_counter : int
            Number of images to call ``normalize_stats``.
        """
        if self.cfg.DATA.TEST.LOAD_GT and self.cfg.TEST.EVALUATE:
            print('Test Accuracy: ', round((self.stats['test_accuracy'] * 100), 2), "%")
            print("Confusion matrix: ")
            print(self.stats['cm'])
            if self.class_names is not None:
                display_labels = ["Category {} ({})".format(i, self.class_names[i]) for i in range(self.cfg.MODEL.N_CLASSES)]
            else:
                display_labels = ["Category {}".format(i) for i in range(self.cfg.MODEL.N_CLASSES)]
            print("\n"+classification_report(self.all_gt, self.all_pred, target_names=display_labels))

    def after_merge_patches(self, pred):
        """
        Steps need to be done after merging all predicted patches into the original image.

        Parameters
        ----------
        pred : Torch Tensor
            Model prediction. 
        """
        pass

    def after_merge_patches_by_chunks_proccess_patch(self, filename):
        """
        Place any code that needs to be done after merging all predicted patches into the original image
        but in the process made chunk by chunk. This function will operate patch by patch defined by 
        ``DATA.PATCH_SIZE``.

        Parameters
        ----------
        filename : List of str
            Filename of the predicted image H5/Zarr.  
        """
        pass

    def after_full_image(self, pred):
        """
        Steps that must be executed after generating the prediction by supplying the entire image to the model.

        Parameters
        ----------
        pred : Torch Tensor
            Model prediction.
        """
        pass
        
    def normalize_stats(self, image_counter):
        """
        Normalize statistics.  

        Parameters
        ----------
        image_counter : int
            Number of images to average the metrics.
        """
        pass