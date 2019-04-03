import cv2
import numpy as np
import sqlite3
recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load("C:\\Python27\\recog2/training2.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataset2'
def getProfile(id):
   conn = sqlite3.connect("facebase.db")
   cmd = "SELECT * FROM Peoples WHERE id = "+str(id)
   cursor = conn.execute(cmd)
   profile = None
   for row in cursor:
       profile = row
   conn.close()
   return profile
cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,1,0,1,1) #Creates a font
while True:
     ret,im = cam.read()
     gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
     faces = faceCascade.detectMultiScale(gray,1.3,5)
     for(x,y,w,h) in faces:
           id, conf = recognizer.predict(gray[y:y+h,x:x+w])
           if(conf<60):
              profile=getProfile(id)
           else:
              id=0
              profile=getProfile(id)
           cv2.rectangle(im,(x,y),(x+w,y+h),(225,255,0),2)
           #profile = getProfile(id)
           if(profile != None):
              cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[1]),(x,y+h+30),font,(0,0,255))
              cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[2]),(x,y+h+60),font,(0,0,255))
              cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[3]),(x,y+h+90),font,(0,0,255))
              cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[4]),(x,y+h+120),font,(0,0,255))
           
     cv2.imshow('Face Recognition',im);
     if (cv2.waitKey(1) == ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()


