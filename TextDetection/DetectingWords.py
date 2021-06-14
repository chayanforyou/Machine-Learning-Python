"""
Detecting Words
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

##############################################
##### Detecting Words  ######
##############################################
# #[   0          1           2           3           4          5         6       7       8        9        10       11 ]
# #['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
boxes = pytesseract.image_to_data(img)
for a,b in enumerate(boxes.splitlines()):
        print(b)
        if a!=0:
            b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)