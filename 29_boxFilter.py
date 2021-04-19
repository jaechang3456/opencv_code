# 이미지를 부드럽게 해주는 필터
import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png')

# 3 X 3 커널 사용할 때
dst1 = cv2.blur(img, (3,3) )

# 7 X 7 커널 사용할 때
dst2 = cv2.blur(img, (7,7) )

combined = np.hstack([img, dst1, dst2])

cv2.imshow("combined", combined)

cv2.waitKey()
cv2.destroyAllWindows()