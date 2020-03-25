import numpy as np
import cv2

# convert image to grayscale
img_obj = cv2.imread('../images/bit-sm.png', cv2.IMREAD_GRAYSCALE)
img_obj_remap = cv2.applyColorMap(img_obj, cv2.COLORMAP_BONE)

# use highgui to display image
cv2.imshow("Jeanne in Gray", img_obj_remap)

# keeps the image displayed
cv2.waitKey(8000)