import cv2
import os
import numpy as np
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
rec = cv2.createLBPHFaceRecognizer()
rec.load("C:\\Python27\\recog/training.yml")
id = 1
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,3,1,0,4)
while True:
    ret,img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = img[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w]
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        
        if(id==1):
            id="Aman"
        if(id==3):
            id="Aman"
        
        else:
            id="unknown"
        cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1) == ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
