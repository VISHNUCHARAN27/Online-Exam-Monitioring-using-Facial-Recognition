import os  # THis library is used to extract paths from the computer
import cv2
import numpy as np
from PIL import Image  #Since we are capturing the images we need the pillow library

recognizer=cv2.face.LBPHFaceRecognizer_create();  #This is the face recognizer of an image in an folder

# We can also use
# EigenFaces – cv2.face.EigenFaceRecognizer_create()
# FisherFaces – cv2.face.FisherFaceRecognizer_create()
# Local Binary Patterns Histograms (LBPH) – cv2.face.LBPHFaceRecognizer_create()
path='C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\USERNAME'

def getImagesWithId(path):
    imgpaths=[os.path.join(path,f) for f in os.listdir(path)]
    #The os.listdir(path) is listing all the directories which are the pictures and fetching all the directories of the pictures
    #The join function concatenates path with a slash and creating a list
    #To check the functionality print(imgpaths)
    faces=[]
    IDs=[]
    for imgpath in imgpaths:   #First we have to open the image and convert it to numpy array
        faceImg=Image.open(imgpath).convert('L');  #We convert it to gray scale image by using 'L'. Already it is in gray scale but we do convert it
        facenp=np.array(faceImg,np.uint8)   #We convert it to a numpy array so that opencv can work with it
        ID=int(os.path.split(imgpath)[-1].split('.')[1])#First the image should be split using path spliter and then using '.' spliter.[-1] means happens from backwards
        #First we split it using path spliter then we use '.' spliter.  We get the 1st index using[1]
        faces.append(facenp)
        IDs.append(ID)
        cv2.imshow("Training",facenp)
        cv2.waitKey(10)
    return np.array(IDs),faces  # We convert integer array of Ids to numpy array as openCv works with only numpy arrays.

IDs,faces=getImagesWithId(path)
recognizer.train(faces,IDs)   #Trains the data
recognizer.write('C:\\Users\\B.Vishnu charan\\Desktop\\VISHNU FILES\\FOURTH SEMESTER\\IMAGE PROCESSING\\FACE IDENTIFICATION\\TRAINER\\traindata.yml')
cv2.destroyAllWindows()






































