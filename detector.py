import cv2
import numpy as np
import pandas as pd
import csv
from datetime import datetime
import time
import sys

face_cascade=cv2.CascadeClassifier("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\HAAR CASCADES\\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\HAAR CASCADES\\haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
roc=cv2.face.LBPHFaceRecognizer_create();
roc.read('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\TRAINER\\traindata.yml')  # Read the data from the trained recognizer
font=cv2.FONT_HERSHEY_SIMPLEX

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
flag=0
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color = frame[y:y + h, x:x + w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            id,conf=roc.predict(gray[y:y+h,x:x+w])  #we predict the id and configuration of the face
            id2 = int(id)
            """
            c = 0
            x = pd.read_csv("C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\users.csv")
            x1 = list(x['idvals'])
            for i in x1:
                if (i != id2):
                    c += 1
                    if (c > 50):
                        print('Not a valid user')
                        row = [-1, 'Invalid', dt_string]
                        with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv','a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()
                        break
            """
            if id == 67:
                row=[id,'Vishnu Charan',dt_string]
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv','a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                flag =1  #'Vishnu Charan'
                break
            if id == 400:
                row = [id, 'Pratyush', dt_string]
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                flag = 1 # 'Pratyush'
                break
            if id==78:
                row = [id, 'Durai', dt_string]
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                flag = 1  #'Durai'
                break
            if id==5:
                row = [id, 'Tharun', dt_string]
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                flag = 1  #'Tharun'
                break
            if id==300:
                row = [id, 'Vanathi', dt_string]
                with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                flag = 1  #'Vanathi'
                break

            #cv2.putText(frame, str(id), (x, y + h), font, 2, (255, 0, 0),5);  # (x,y+h) displays the coordinates below the face. Fifth argument is the font size
            #cv2.imshow('Image', frame)

    time.sleep(1)
    break
    #if(cv2.waitKey(1)==27):


#print(id)
#wer = pd.read_csv('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv')
#wer2 = list(wer['id'])
#print(wer2[-1])

if(flag==0):
    print('Not a valid user')
    row = [-1, 'Invalid', dt_string]
    with open('C:\\Users\\B.Vishnu charan\\PycharmProjects\\Face_detection\\idvals.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


cv2.destroyAllWindows()
cap.release()
sys.exit()


"""
Comment section
"""
"""
         
                        cv2.destroyAllWindows()
                        cap.release()

            if id==1:
                id='Vishnu Charan'
            if id==2:
                id='Dheshan'
            if id==5:
                id='Gautham'
            if id==6:
                id='Anunay'
            if id==9:
                id='Shylesh'
            if id==7:
                id='Arun Balaji'
            if id==14:
                id='ajeethra'
            if id==56:
                id='Keshav'
            if id==100:
                id='Aniv'
            if id==344:
                id='Abrar'
            if id==34:
                id='bvc'
            if id==111:
               id='Pratyush'
            if id==120:
                id='Aditya'
            if id==500:
                id="usha"
            if id==67:
                id="Vischa"
            cv2.putText(frame,str(id),(x,y+h),font,2,(255,0,0),5);    #(x,y+h) displays the coordinates below the face. Fifth argument is the font size
            
    cv2.imshow('Image',frame)
    
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cap.release()
"""




"""
            if id == 67:
                id = 'Vishnu Charan'
            if id==400:
                id = 'Pratyush'
            if id==200:
                id = 'Sir'
            cv2.putText(frame, str(id), (x, y + h), font, 2, (255, 0, 0),5);  # (x,y+h) displays the coordinates below the face. Fifth argument is the font size
"""


"""

id2 = int(id)
            c = 0
            x = pd.read_csv("C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\projectdatabase.csv")
            x1 = list(x['User_id'])
            x2 = list(x['Key'])
            for i in x1:
                if (i != id2):
                    c += 1
                    if (c > 50):
                        print("Not a valid user")
                        break
                elif (i == id2):
                    print(i)

                    # *while True:
                    x = input("Do you want to send message(Press s) or receive the message(Press r): ")
                    # if(x!='s' or x!='r'):
                    #   print("Please enter s or r")
                    #  continue
                    # else:
                    # print('validated')
                    if (x == 's'):
                        message = input("Enter the message: ")
                        r_id = int(input("Enter the receiver id: "))
                        c = x1.index(r_id)
                        d = x2[c]
                        result = ""
                        print(d)
                        for i in range(len(message)):
                            char = message[i]
                            if (char.isupper()):
                                result += chr((ord(char) + d - 65) % 26 + 65)
                            else:
                                result += chr((ord(char) + d - 97) % 26 + 97)

                        row = [id2, r_id, result]
                        with open('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\messagedatabase.csv','a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(row)
                        csvFile.close()

                        cv2.destroyAllWindows()
                        cap.release()

                    elif (x == 'r'):
                        c = x1.index(id2)
                        d = x2[c]

                        receiver = pd.read_csv('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\messagedatabase.csv')

                        y1 = list(receiver['Receiver_id'])
                        # print("y1=",y1)
                        y2 = y1.index(id2)

                        y3 = list(receiver['Sender_id'])
                        # print("y3=",y3)
                        sender = y3[y2]

                        enc_msg_list = list(receiver['Encrypted_message'])
                        enc_msg = enc_msg_list[y2]

                        result = " "
                        # print(d)
                        for i in range(0, len(enc_msg)):
                            char = enc_msg[i]
                            if (char.isupper()):
                                result += chr((ord(char) - d + 65) % 26 + 65)
                            elif (char.islower()):
                                char1 = char.upper()
                                char2 = chr((ord(char1) - d + 65) % 26 + 65)
                                char3 = char2.lower()
                                result += char3

                        print("The message you received from sender_id:",sender," is:,"end='')
                        print('"{}"'.format(result))

    cv2.imshow('Image', frame)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cap.release()
"""