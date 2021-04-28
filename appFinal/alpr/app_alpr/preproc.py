import os
import cv2
import numpy as np
from PIL import Image, ImageFilter

def preproc(src_folder, dest_folder):
    img = cv2.imread(os.path.join(src_folder,'pred.png'),0)
    thresh1= 128
    thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        if cv2.contourArea(c) < 10:
            cv2.drawContours(thresh, [c], -1, (0,0,0), -1)
    result = 255 - thresh
    img = cv2.threshold(result, thresh1, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite(os.path.join(dest_folder,'preproc.png'),img)