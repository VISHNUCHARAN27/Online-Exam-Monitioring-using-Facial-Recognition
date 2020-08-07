# We first create the dataset
# Then we train the dataset
#Then we detect the data in the current frame
import cv2
import numpy as np
import random
import pandas as pd
import csv

face_cascade=cv2.CascadeClassifier("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\HAAR CASCADES\\haarcascade_frontalface_default.xml") # A trained model for face detection
eye_cascade=cv2.CascadeClassifier("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\HAAR CASCADES\\haarcascade_eye.xml") # A trained model for eye detection

cap=cv2.VideoCapture(0)  # Used to capture image from web camera. Generally the initial camera value is 0.
id=input('Enter user-id:')
sampleNum=0

name=input('Enter your name:')


key_list=[]
for i in range(1,101):
    key_list.append(i)


check=pd.read_csv("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\projectdatabase.csv")
key_check=list(check['Key']);


key=random.choice(key_list)
while(key in key_check):
    key=random.choice(key_list)

row = [id,key,name]

with open('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\projectdatabase.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()

database=pd.read_csv("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\projectdatabase.csv")
database.to_csv("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\projectdatabase.csv",index=False)

key_list.remove(key)


while True:
    ret,frame=cap.read()  #cap.read will return one status variable and capture image from the camera
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #We convert it to grayscale image because classifier works only with gray scale image
    faces=face_cascade.detectMultiScale(gray)  # This will detect all the faces in the current frame and will return the co-ordinates of the frame.
    # We are getting the face coordinates and drawing a rectangle over them.
    for x,y,w,h in faces:
        sampleNum=sampleNum+1
        cv2.imwrite('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\USERNAME\\'+'User.'+ str(id) +'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)    #(x,y) is the initial point of the rectangle. Final point is (x+w,y+h). 3 is the thickness
        roi_gray=gray[y:y+h,x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.waitKey(100)
    cv2.imshow('Image',frame)
    cv2.waitKey(1)
    if(sampleNum>50):
        break
cv2.destroyAllWindows()
cap.release()







#database.columns=['User_id','key']
#db_values=pd.DataFrame()
#db_values.colu
#db_values['User_id']=id
#db_values['key']=key
#db_values['name']=name

