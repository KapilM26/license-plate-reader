import os
from pytesseract import image_to_string
from PIL import Image

def ocr(src_folder):
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options += " --psm 7"
    no = image_to_string(Image.open(os.path.join(src_folder,"preproc.png")),config=options)
    return no
    