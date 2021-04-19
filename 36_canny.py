import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg', 0)

cv2.imshow('gray', img)

threshold_1 = 120 # high : 0~255 중에 설정

threshold_2 = 100 # low : 200

result = cv2.Canny(img, threshold_1, threshold_2)

cv2.imshow("Canny", result)

cv2.waitKey()
cv2.destroyAllWindows()