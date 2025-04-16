from turtledemo.nim import COLOR

import cv2
# for image

# img = cv2.imread("Resources/aigenblogapp.png")
# cv2.imshow("image",img)
# cv2.waitKey(0)


# for a video
# frameWidth= 640
# frameHeight = 360
#
# cap = cv2.VideoCapture("Resources/meme.mp4")
# while True:
#     sucess,img = cap.read()
#     # if image reading is sucessfull it will declare success as true else false
#     cv2.imshow("Video",img)
#
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
#         # if we will press q it will break and other wise infinite loop

# for web cam



# import cv2
#
# frameWidth = 640
# frameHeight = 480
#
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
#
# while True:
#     success, img = cap.read()
#
#     if not success:
#         print("Failed to read from camera")
#         break
#
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#############################################################

# import cv2
# import numpy as np
#
# kernel  = np.ones((5,5),np.uint8)
# print(kernel)
# # this 5 will be a 5 cross 5 matrix of 1's
# path = "Resources/aigenblogapp.png"
# img = cv2.imread(path)
# # we can write (path,0) in imread if u want to change the image in greyscale
# # or we can use this
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY )
# #  for blur image
# imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
# #  canny image
# imgCanny = cv2.Canny(imgBlur,100,100)
# #  image dilation
# # isme we need to declare a matrix and for that we need to import numpy
# imgDilation  = cv2.dilate(imgCanny,kernel,iterations=1)
# #  the more the iteations the more the thicknees of lines will incrrease
# cv2.imshow("image",img)
# cv2.imshow("GRAY IMAGE",imgGray)
# cv2.imshow("blur IMAGE",imgBlur)
# cv2.imshow("Canny IMAGE",imgCanny)
# cv2.imshow("Dilation IMAGE",imgDilation)
# cv2.waitKey(0)


#############################################################

# crop resize image

# RESIZE
# import cv2
# path = "Resources/aigenblogapp.png"
#
# img = cv2.imread(path)
# width , height = 400 ,400
# imgResize = cv2.resize(img,(width,height))
#
#
# # cv2.imshow("Image",img)
# cv2.imshow("Image",imgResize)
# print(imgResize.shape)
# cv2.waitKey(0)

# CROPING THE IMAGE

import cv2
path = "Resources/aigenblogapp.png"
img = cv2.imread(path)
imgCropped = img[0:200,200:540]
# first x wala and 2nd y wala


# generate the code for resize image