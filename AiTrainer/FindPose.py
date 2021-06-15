"""
Pose Detection From Image
By: Chayan Mistry
Youtube: http://www.youtube.com/c/chayanforyou
Website: https://chayanforyou.github.io/
"""

import cv2
import PoseModule as pm

detector = pm.poseDetector()

while True:
    img = cv2.imread("files/test.jpg")
    img = detector.findPose(img, True)
    lmList = detector.findPosition(img, False)
    print(lmList)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
