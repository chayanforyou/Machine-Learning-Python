"""
Face Recognition Basic
By: Chayan Mistry
Youtube: http://www.youtube.com/c/chayanforyou
Website: https://chayanforyou.github.io/

pip install cmake
pip install dlib>=19.8
In visual studio, Individual Components tab,Visual C++ tools for Cmake checkbox under Compilers,build tools and runtimes Section
On Visual Studio Command prompt run, pip install face_recognition

Source: https://stackoverflow.com/a/52429058/5280371
Download Link: https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16

"""

import cv2
import face_recognition
 
imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Bill gates.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodeElon],encodeTest)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)