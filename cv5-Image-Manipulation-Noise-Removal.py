# python cv5-Image-Manipulation-Noise-Removal.py

# we study noise removal one of the branch of Image manipulation
import numpy as np
import cv2
# from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

lion_img = cv2.imread("image/lion.jpg")
print(lion_img.shape)
# cv2_imshow(lion_img)
# cv2.imshow("lion_img",lion_img)


# Image Denoising
# it apply noising filter 
# it remove large extent by its averaging pixels by  taking mean of pixel in that area and denoising it
"""
Modification of fastNlMeansDenoising function for colored images.

Parameters
    src	            Input 8-bit 3-channel image.
    dst	            Output image with the same size and type as src .
    h_luminance	    Parameter regulating filter strength. Big h value perfectly removes noise but also removes image details, smaller h value preserves details but also preserves some noise
    photo_render	  float The same as h but for color components. For most images value equals 10 will be enough to remove colored noise and do not distort colors
    search_window	  Size in pixels of the window that is used to compute weighted average for given pixel. Should be odd. Affect performance linearly: greater search_window - greater denoising time. Recommended value 21 pixels
    block_size	    Size in pixels of the template patch that is used to compute weights. Should be odd. Recommended value 7 pixels
    stream	        Stream for the asynchronous invocations.

"""

denoise = cv2.fastNlMeansDenoisingColored(lion_img , None , 19,10 ,21 ,7)
display2 = np.hstack((lion_img , denoise))
# cv2_imshow(display2)
cv2.imshow("Both image before & After noise Removal",display2)