import cv2
import numpy as np

img = cv2.imread('data/images/truth.png')

cv2.imshow('ori',img)

sobelx = cv2.Sobel(img,cv2.CV_32F, 1, 0)

sobely = cv2.Sobel(img,cv2.CV_32F, 0, 1)

cv2.imshow('sobel X', sobelx)

cv2.imshow('sobel Y', sobely)

cv2.waitKey()
cv2.destroyAllWindows()