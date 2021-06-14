"""
Image To String
By: Chayan Mistry
Youtube: http://www.youtube.com/c/chayanforyou
Website: https://chayanforyou.github.io/

Installation: https://tesseract-ocr.github.io/tessdoc/Home.html
For Windows : https://github.com/UB-Mannheim/tesseract/wiki
"""

import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pytesseract
##############################################
##### Image to String   ######
##############################################
print(pytesseract.image_to_string(img))
cv2.imshow('img', img)
cv2.waitKey(0)