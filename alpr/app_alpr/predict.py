import torch
from .apps import ModelConfig
from torch.utils.data import DataLoader
from .yolo.utils.datasets import *
from .yolo.models import *
from .yolo.utils.utils import *
from .yolo.utils.datasets import *
from torchvision import datasets
from torch.autograd import Variable
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator
import numpy as np
from PIL import Image

def predict(src_folder, dest_folder, model_folder):
    dataloader = DataLoader(ImageFolder(src_folder),
                            batch_size=1,
                            shuffle=False)

    classes = load_classes(os.path.join(model_folder,'classes.names'))  # Extracts class labels from file

    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    imgs = []  # Stores image paths
    img_detections = []  # Stores detections for each image index

    for batch_i, (img_paths, input_imgs) in enumerate(dataloader):
        # Configure input
        input_imgs = Variable(input_imgs.type(Tensor))

        # Get detections
        with torch.no_grad():
            detections = ModelConfig.model(input_imgs)
            detections = non_max_suppression(detections, conf_thres=0.5, nms_thres=0.4)


        # Save image and detections
        imgs.extend(img_paths)
        img_detections.extend(detections)


    # Iterate through images and save plot of detections
    for img_i, (path, detections) in enumerate(zip(imgs, img_detections)):
        img = np.array(Image.open(path))

        # Draw bounding boxes and labels of detections
        if detections is not None:
            # Rescale boxes to original image
            detections = rescale_boxes(detections, 416, img.shape[:2])
            (x1, y1, x2, y2, conf, cls_conf, cls_pred) = detections[0]
            im = Image.fromarray(img)
            im1 = im.crop((x1.data.tolist(),y1.data.tolist(),x2.data.tolist(),y2.data.tolist()))
            im1 = im1.save(os.path.join(dest_folder,"pred.png"))