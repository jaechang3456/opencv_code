import cv2
import numpy as np

img = cv2.imread('data/images/mountain.jpeg')

cv2.imshow("ori", img)

sharpen = np.array(
    [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ] , dtype='int' )

result = cv2.filter2D(img, -1, sharpen)

cv2.imshow("sharp", result)

cv2.waitKey()
cv2.destroyAllWindows()