import cv2
import sys
import time
import pandas as pd
import csv
import os

faceCascade = cv2.CascadeClassifier('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\HAAR CASCADES\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
img_count=0

cheatvideopath="C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\Cheatvideos\\Outputs.avi"
codec=cv2.VideoWriter_fourcc('X','V','I','D')
framerate=30
resolution=(640,480)
VideofileOutput=cv2.VideoWriter(cheatvideopath,codec,framerate,resolution)

now = time.time()
future = now + 10

if (cap.isOpened()):
    ret, frame = cap.read()
else:
    ret = False

while ret:
    # Capture frame-by-frame
    temp_count=0
    ret, frame = cap.read()

    VideofileOutput.write(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        temp_count += 1
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if(temp_count>img_count):
        img_count=temp_count

    # Display the resulting frame
    #cv2.imshow('FaceDetection', frame)

    if(time.time() > future):
        x = pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv')
        x1 = list(x['id'])
        x2 = int(x1[-1])

        if(x2!=-1):
            row = [x2,img_count]
            with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\noofface.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
        ret=False
        break


# When everything is done, release the capture
cap.release()
VideofileOutput.release()


x = pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\noofface.csv')
x1 = list(x['Nooffaces'])
x2 = int(x1[-1])
if (x2 == 1):
    os.remove("C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\Cheatvideos\\Outputs.avi")





