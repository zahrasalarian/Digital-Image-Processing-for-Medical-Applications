import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
Detecting Circles in the Limbal Dermoid Image using Hough Transform

1. Image Loading: 
    - Read the grayscale image 'limbal-dermoid.jpeg'.

2. Preprocessing:
    - Apply a median blur to the image to reduce noise.

3. Hough Circle Detection:
    - Utilize OpenCV's HoughCircles function with the following parameters:
        - Method: HOUGH_GRADIENT
        - dp: 1.5 (Inverse ratio of the accumulator resolution to the image resolution)
        - minDist: 20 (Minimum distance between the centers of the detected circles)
        - param1: 700 (Higher threshold for the internal Canny edge detection)
        - param2: 30 (Threshold for the circle accumulator)
        - minRadius: 30 (Minimum circle radius)
        - maxRadius: 35 (Maximum circle radius)

4. Circle Annotation:
    - Draw the detected circles and their centers on the image.

5. Display:
    - Show the annotated image with detected circles.

Optimization Strategy:
    - Initial parameter values are carefully chosen.
    - Adjustments are made through trial and error to minimize false positives and maximize detection sensitivity.
"""

color = (0, 0, 255)

# Image Loading
limbal_dermoid_img = cv2.imread('limbal-dermoid.jpeg', 0)
assert limbal_dermoid_img is not None, "file could not be read, check with os.path.exists()"

# Preprocessing
img = cv2.medianBlur(limbal_dermoid_img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
# Hough Circle Detection
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.5,20,param1=700,param2=30,minRadius=30,maxRadius=35)
circles = np.uint16(np.around(circles))

# Circle Annotation
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],color,2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(255, 0, 0),3)

# Display
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()