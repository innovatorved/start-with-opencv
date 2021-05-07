# python cv3-Edge-Detection-canny-erosion-dilute.py

import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
import matplotlib.pyplot as plt

img4 = cv2.imread("image/light.jpg")
print(img4.shape)
# cv2_imshow(img4)

#Canny_Edge_detection on image
#Cannyimage does not display we want to convert in any format like grey scale
#it only works on grey scale image
# it supoose image is grey scale
grey_img4 = cv2.cvtColor(img4 , cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(grey_img4 ,150,200)
# print(canny_image.shape)
# cv2_imshow(canny_image)
cv2.imshow("canny_image" , canny_image)
# matrix manipulation bby opencv
# Erosion and Dilation
# genrate wwindow size for erosion

# Erosion
# Remove Pixels from Boundaries
# ersosion genrally use to remove noise better with dilation
kernel = np.ones((1,1),np.uint8)
erode_image = cv2.erode(canny_image ,kernel , iterations = 1 )
# cv2_imshow(erode_image)
cv2.imshow("erode_image" , erode_image)


# Dialtion 
# Add pixels in Boundaries
kernel2 = np.ones((5,5),np.uint8)
dilate_image = cv2.dilate(canny_image , kernel2 , iterations = 1)
# cv2_imshow(dilate_image)
cv2.imshow("dilate_image" , dilate_image)