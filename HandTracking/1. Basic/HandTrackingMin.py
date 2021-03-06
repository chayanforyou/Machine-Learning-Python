"""
Hand Tracing Basic
By: Chayan Mistry
Youtube: http://www.youtube.com/c/chayanforyou
Website: https://chayanforyou.github.io/
"""

import cv2
import mediapipe as mp
import datetime
import numpy as np

# 0 : capture video from laptop default camera
cap = cv2.VideoCapture(0)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    # default = 2
    max_num_hands=2,
    # Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully (default= 0.5)
    min_detection_confidence=0.5,
    # Minimum confidence value ([0.0, 1.0]) from the hand detection model for the detection to be considered successful. (default = 0.5)
    min_tracking_confidence=0.5
    )
mpDraw = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0

# initialize time and frame count variables
last_time = datetime.datetime.now()
frames = 0
 
while True:
    # blocks until the entire frame is read
    success, img = cap.read()
    frames += 1
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
 
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(abs(lm.z) * w)
                # print(id, cx, cy)
                if id == 0:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
 

    # compute fps: current_time - last_time
    delta_time = datetime.datetime.now() - last_time
    elapsed_time = delta_time.total_seconds()
    cur_fps = np.around(frames / elapsed_time, 1)
 
    # cv2.putText(img, str(cur_fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.putText(img, 'FPS: ' + str(cur_fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)