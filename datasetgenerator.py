import cv2
import numpy as np
import sqlite3

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def insertOrUpdate(id, Name , Age, Gender, Designation):
    conn = sqlite3.connect("facebase.db")
    cmd = "SELECT * FROM Peoples WHERE id = " + str(id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE Peoples SET Name =" + str(Name) + "WHERE ID= " + str(id)
    else:
        cmd = "INSERT INTO Peoples(id,Name,Age,Gender,Designation) Values(" + str(id) + "," + str(Name) + "," + str(Age) + "," + str(Gender) + "," + str(Designation)+")"  
    conn.execute(cmd)
    conn.commit()
    conn.close()


id = raw_input('enter your id\n')
Name = raw_input('enter your name\n')
Age = raw_input('enter your Age\n')
Gender = raw_input('enter your Gender\n')
Designation = raw_input('enter your Designation\n')

insertOrUpdate(id, Name, Age, Gender, Designation)
sample = 0
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sample = sample + 1
        cv2.imwrite("dataSet2/user." + str(id) + '.' + str(sample) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
        cv2.waitKey(100)
    cv2.imshow('img', im)

    if (sample > 5):
        break
cam.release()
cv2.destroyAllWindows()

