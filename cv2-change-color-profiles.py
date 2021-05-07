# python cv2-change-color-profiles.py

import cv2
# from google.colab.patches import cv2_imshow

# changing Gray Scale
img2 = cv2.imread("image/img1.jpg")
ch_gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
cv2.imshow("ch_gray",ch_gray)
# cv_imshow(ch_gray)

# if we change image BGR 2 Gray we compress 3 channel into single channel
# these channels contain information of Red , Blue and Green color info of image
# we have reduce no.  of channelss also information and pixels

print(f"Shape of RGB {(img2.shape)} and Shape of Grey {ch_gray.shape}")

IMG3 = cv2.cvtColor(img2 , cv2.COLOR_BGR2RGBA)
print(IMG3.shape)
cv2.imshow("img3" , IMG3)
# cv_imshow(IMG3)

# HSL image
# also 3 channels but color info is define on single bit
# convert ch_gray into hsv image
# HSV stands for: HUE SATURATION VARIANCE
hsv = cv2.cvtColor(img2 , cv2.COLOR_BGR2HSV)
print(hsv.shape)

# cv_imshow(hsv)
cv2.imshow("hsv",hsv)

