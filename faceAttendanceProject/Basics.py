import cv2
import numpy as np
import face_recognition

imageElon = face_recognition.load_image_file("imageBasics/elon.png")
imageElon = cv2.cvtColor(imageElon,cv2.COLOR_BGR2RGB)
imageTest = face_recognition.load_image_file("imageBasics/img_2.png")
imageTest = cv2.cvtColor(imageTest,cv2.COLOR_BGR2RGB)

# step 2  finding the faces and finding their encoding and face distances

faceLoc = face_recognition.face_locations(imageElon)[0]
# we r sending only one image toh we will get only first element of the image
encodeElon = face_recognition.face_encodings(imageElon)[0]
cv2.rectangle(imageElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imageTest)[0]
# we r sending only one image toh we will get only first element of the image
encodeElonTest = face_recognition.face_encodings(imageTest)[0]
cv2.rectangle(imageTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

# step -3 compare the encoding of the iamges

results = face_recognition.compare_faces([encodeElon],encodeElonTest)
print(results[0])


# sometimes what happens is that we have very large amount of images in that case we cant compare each so we find how similar each image is
# by finding the distances
# concept is the lower the distances the better the match
faceDistance = face_recognition.face_distance([encodeElon],encodeElonTest)
print(faceDistance)
label = "Match" if results[0] else "No Match"
cv2.putText(
    imageTest,
    f'{label} ({round(faceDistance[0], 2)})',
    (50, 50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 255, 0) if results[0] else (0, 0, 255),
    2
)


cv2.imshow("Elon Musk",imageElon)
cv2.imshow("Elon  Test",imageTest)
cv2.waitKey(0)