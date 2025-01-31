import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load("C:\\Python27\\recog/training.yml")
id = 1
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,4)

while True:
    ret,img=cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",img)
    if(cv2.waitKey(1)==27):
        break
cam.release()
cv2.destroyAllWindows()
