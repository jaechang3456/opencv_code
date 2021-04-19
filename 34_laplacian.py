import cv2
import numpy as np

img = cv2.imread('data/images/truth.png')

laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize=3, scale=1)

cv2.imshow('ori', img)
cv2.imshow('lapl', laplacian)

cv2.waitKey()
cv2.destroyAllWindows()