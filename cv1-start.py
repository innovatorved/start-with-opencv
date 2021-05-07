# python cv1-start.py
import cv2
# import numpy as np
# from google.colab.patches import cv2_imshow

# read img : cv2.imread(__img-path-name__)
img = cv2.imread("image/color.jpg")

# show image : cv2_imshow(__name of read image__)
cv2.imshow(img)

# check the Dimensions of image
print(img.shape)