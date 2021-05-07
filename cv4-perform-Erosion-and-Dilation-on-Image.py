# python cv4-perform-Erosion-and-Dilation-on-Image.py

import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
# import matplotlib.pyplot as plt


# Always erosio after Dilated image
# first add pixels in boundaries by Dialation then remove pixels from boundaries by erosion
# select img light2.jpg

# firsdt read the image
# image/light.jpg
my_img = cv2.imread("image/color.jpg")
print(my_img.shape)  # shape of image

# change image in to grey scale for performing Canny
grey_my_img = cv2.cvtColor(my_img , cv2.COLOR_BGR2GRAY)

# Change Grey Scale image into Canny Image
canny_my_img = cv2.Canny(grey_my_img , 150 , 200)
# cv2_imshow(canny_my_img)
# cv2.imshow("canny_my_img",canny_my_img)

# perform Dilation first 
# make window or kernel
kernel = np.ones((5,5) ,np.uint8)
dilate_my_img = cv2.dilate(canny_my_img , kernel , iterations = 1)
# cv2_imshow(dilate_my_img)
# cv2.imshow("dilate_my_img",dilate_my_img)


# then perform Erosion
erosion_my_img = cv2.erode(dilate_my_img , kernel , iterations = 1)
# cv2_imshow(erosion_my_img)
# cv2.imshow("erosion_my_img",erosion_my_img)


# show these all image horizentaly by np.hstach fun
# cv2_imshow(my_img)
display = np.hstack((grey_my_img ,canny_my_img , dilate_my_img , erosion_my_img))
# cv2_imshow(display)
cv2.imshow("Display All Horizentally",display)

"""
# create figure with matplotlib
fig = plt.figure(figsize=(20,10))
rows = 2
columns = 2

fig.add_subplot(rows, columns, 1)
plt.imshow(grey_my_img)

fig.add_subplot(rows, columns, 2)
plt.imshow(canny_my_img)

fig.add_subplot(rows, columns, 3)
plt.imshow(dilate_my_img)

fig.add_subplot(rows, columns, 4)
plt.imshow(erosion_my_img)

plt.show()"""