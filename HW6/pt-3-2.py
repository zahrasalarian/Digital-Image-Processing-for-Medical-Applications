import cv2
import numpy as np
import matplotlib.pyplot as plt

color = (0, 0, 255)

### 7. Load limbal-dermoid image
limbal_dermoid_img = cv2.imread('limbal-dermoid.jpeg', 0)
assert limbal_dermoid_img is not None, "file could not be read, check with os.path.exists()"

### 8. Test different results for different input parameters for the cv.HoughCircles function
img = cv2.medianBlur(limbal_dermoid_img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.5,20,param1=700,param2=30,minRadius=30,maxRadius=35)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],color,2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(255, 0, 0),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()