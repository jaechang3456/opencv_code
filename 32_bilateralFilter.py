# 이미지를 부드럽게 해주는 필터
import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

result = cv2.bilateralFilter(img, 15, 80, 80)

combined = np.hstack([img, result])

cv2.imshow("combined", combined)

cv2.waitKey()
cv2.destroyAllWindows()