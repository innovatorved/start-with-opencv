# python cv5-Drawing-Functions-circle-rectangle-line-text.py
import cv2
# from google.colab.patches import cv2_imshow
import numpy as np
import matplotlib.pyplot as plt

# create black image
image_black = np.zeros((512 , 512 ,3) , np.uint8) # black box of 512 * 512 
cv.imgshow("Black 512*512 *3 image created" ,image_black )


# Draw a Circle
# cv2.circle(__img-source__ , __circle-center-by-x-y__ ,__radius__ , __colour__(blue , green , red),thickness)
cv2.circle(image_black , (100,100) ,50 , (50 , 255 , 120) , 10)
# cv2_imshow(image_black)
cv.imgshow("Circle Added" ,image_black )


# Draw a rectangle
"""
rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
.   @brief Draws a simple, thick, or filled up-right rectangle.
.   
.   The function cv::rectangle draws a rectangle outline or a filled rectangle whose two opposite corners
.   are pt1 and pt2.
.   
.   @param img Image.
.   @param pt1 Vertex of the rectangle. is the up-left coordinates of an rectangle
.   @param pt2 Vertex of the rectangle opposite to pt1 . is the down-right coordinates of and rectangle
.   @param color Rectangle color or brightness (grayscale image).
.   @param thickness Thickness of lines that make up the rectangle
"""
cv2.rectangle(image_black ,(200 ,200) ,(400,400) ,(255,0,0) , 5)
# cv2_imshow(image_black)
cv.imgshow("rectangle Added" ,image_black)

# Draw a line
"""
line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
.   @brief Draws a line segment connecting two points.
.   
.   The function line draws the line segment between pt1 and pt2 points in the image. The line is
.   clipped by the image boundaries. For non-antialiased lines with integer coordinates, the 8-connected
.   or 4-connected Bresenham algorithm is used. Thick lines are drawn with rounding endings. Antialiased
.   lines are drawn using Gaussian filtering.
.   
.   @param img Image.
.   @param pt1 First point of the line segment.
"""
cv2.line(image_black , (100,100) ,(400 , 100) , (0,0,255) , 2)
# cv2_imshow(image_black)
cv.imgshow("line Added" ,image_black )

# Write text on an Image
"""
putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
.   @brief Draws a text string.
.   
.   The function cv::putText renders the specified text string in the image. Symbols that cannot be rendered
.   using the specified font are replaced by question marks. See #getTextSize for a text rendering code
.   example.
.   
.   @param img Image.
.   @param text Text string to be drawn.
.   @param org Bottom-left corner of the text string in the image.
.   @param fontFace Font type, see #HersheyFonts.
.   @param Scale fontsize
.   @param Colour (B,G,R) value
.   @param Thickness of font
"""
cv2.putText(image_black , "Ved Prakash Gupta" , (300,480) , cv2.FONT_HERSHEY_COMPLEX , 0.5 ,(255,120,115) , 1)
# cv2_imshow(image_black)
cv.imgshow("Text Added" ,image_black )