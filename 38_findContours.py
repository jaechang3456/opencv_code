import cv2
import numpy as np
import random

threshold = 0

maxThreshold = 255*3

random.seed(12345)

def callback() :
    # 캐니 에지로, 에지 검출하고,
    imCanny = cv2.Canny(img, threshold, threshold*2, apertureSize=3)
    
    # 컨투어스 연결시킨다. 에지를 연결시킴
    contours, heirarch = cv2.findContours(imCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 연결시켜서 그린다.
    display = np.zeros( (imCanny.shape[0], imCanny.shape[1]) ) 

    for i in range(0, len(contours)) :
        lineColor = (255,0,0)
        cnt = contours[i]
        cv2.drawContours(display, [cnt], -1, lineColor, 2)

    cv2.imshow("Contours", display / 255.0)

def updateHighThreshold(*args) :
    global threshold
    threshold = args[0]
    callback()

img = cv2.imread('data/images/threshold.png', 0)

cv2.namedWindow("Contours", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Contours", img)

cv2.createTrackbar("Canny and Contours", "Contours", threshold, maxThreshold, updateHighThreshold)
callback()

cv2.waitKey()
cv2.destroyAllWindows()