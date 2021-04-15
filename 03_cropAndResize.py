import cv2

source = cv2.imread("data/images/sample.jpg", 3)

# 1은 100%, 0.6은 60%, 1.8은 180% 확대/축소 가능
scaleX = 0.6
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Original", source)

cv2.imshow("Scale Down", scaleDown)

scaleX = 1.8
scaleY = 1.8

scaleUP = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Scale Up", scaleUP)

# 내가 원하는 부분의 이미지를 가져오기

crop_img = source[ 10:200 , 150:250 ]

cv2.imshow("Cropped Img", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()