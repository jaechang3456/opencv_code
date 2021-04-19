import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg', 1)

beta = -100

# 컬러 스페이스 변경
ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 가공을 위해서 uint8을 float으로 변경
ycbImage = np.float32(ycbImage)

# 채널 분리
Ychannel, Cr, Cb = cv2.split(ycbImage)

# 밝기 조절
Ychannel = np.clip(Ychannel + beta, 0, 255)

# 다시 채널 합친다.
ycbImage = cv2.merge( [Ychannel, Cr, Cb] )

# 다시 uint8로 변경
ycbImage = np.uint8(ycbImage)

# 화면 표시를 위해서 컬러스페이스 BGR로 변경
ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

#아래는 이미지를 각각의 윈도우에 표시한 것.
cv2.imshow('src', img)
cv2.imshow('dst', ycbImage)

# 아래는 하나의 윈도우에, 2개의 이미지를 옆(수평)붙여서 표시.
# img_all = np.hstack( [ img, ycbImage ] )
# cv2.imshow('combined', img_all)

# 아래는 하나의 윈도우에, 2개의 이미지를 아래(수직)붙여서 표시.
# img_all = np.vstack( [ img, ycbImage ] )
# cv2.imshow('combined', img_all)

cv2.waitKey()
cv2.destroyAllWindows()