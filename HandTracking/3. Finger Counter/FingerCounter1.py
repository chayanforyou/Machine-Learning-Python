"""
OpenCV Finger Counter
By: Chayan Mistry
Youtube: http://www.youtube.com/c/chayanforyou
Website: https://chayanforyou.github.io/
"""

import cv2
import time
import os
import HandTrackingModule as htm
 
wCam, hCam = 640, 480
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
 
detector = htm.handDetector(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]

def one():
    return "One"
 
def two():
    return "Two"
 
def three():
    return "Three"
 
def four():
    return "Four"
 
def five():
    return "Five"


def numbers_to_strings(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Nothing")
    # Execute the function
    return func()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        # print(fingers)
        totalFingers = fingers.count(1)
        print(f'Finger: {totalFingers}')
 
        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
        
        # make rectangle around all the points
        x_max = 0
        y_max = 0
        x_min = img.shape[0]
        y_min = img.shape[1]
        for point in lmList:
            x, y = point[1], point[2]
            if x > x_max:
                x_max = x
            if x < x_min:
                x_min = x
            if y > y_max:
                y_max = y
            if y < y_min:
                y_min = y
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
        
        # show finger number
        cv2.putText(img, numbers_to_strings(totalFingers), (x_min, (y_min - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
 
    # calculate fps
    cTime = time.time()
    differ = cTime - pTime
    fps = 1 / (differ if differ != 0 else 1)
    pTime = cTime
 
    cv2.putText(img, f'FPS: {int(fps)}', (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    