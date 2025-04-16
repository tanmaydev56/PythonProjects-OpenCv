import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = "imageAttendance"
images = []
classNames =[]
myList =  os.listdir(path) #will print all the images names
for cls in myList:
    currentImage = cv2.imread(f'{path}/{cls}')
    # explain the above line
    images.append(currentImage)
    classNames.append(os.path.splitext(cls)[0])
    # will give first name like jpg and png hat jayega

# step -2 now the encoding process


def finEncodings(images):
    encodeList =[]
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def MarkAttnedance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList =[]
        # print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dateString}')

# MarkAttnedance('Elon')


encodeListForKnownFaces = finEncodings(images)
print("the Encoding has been completed")

#  step - 3 find  the match or compare the photos
# and test images webcame se ayengi and tehn web cam  wali images compare hogi original wali se

cap = cv2.VideoCapture(0)
while True:
    sucess,img = cap.read()
#     now reduce the size of the image
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurrentFrame = face_recognition.face_locations(imgS)
#     find the encodings of the webcam
    encodeCurrentFrame =  face_recognition.face_encodings(imgS,faceCurrentFrame)
#     now compare the matches
    for encodeFace,faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListForKnownFaces,encodeFace)
        faceDis = face_recognition.face_distance(encodeListForKnownFaces,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            # rectangle ki position kharabh aye gi bcz we hv scaled down the image by 0.25 toh waps lane ke liye multiply it by 4

            y1, x2, y2, x1 =  y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            MarkAttnedance(name)
        cv2.imshow('Webcam',img)

        cv2.waitKey(1)
