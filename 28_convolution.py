import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

# cv2.imshow("img", img)

kernel_size = 5

kernel = np.ones( ( kernel_size, kernel_size ) ) / kernel_size**2

print(kernel)

# 컨볼루션! cv2.filter2D 함수
result = cv2.filter2D(img, -1, kernel)

combined = np.hstack([img, result])
cv2.imshow('combined', combined)

cv2.waitKey()
cv2.destroyAllWindows()