import cv2
import numpy as np

img = cv2.imread('data/images/capsicum.jpg', 1)

cv2.imshow("original", img)

saturatuonScale = 0.01

hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsvImage = np.float32(hsvImage)

# 채널로 분리하는 함수 
H, S, V = cv2.split(hsvImage)

# 유용한함수 : np.clip 함수를 이용 0보다 작으면 0으로 맞추고
# 255보다 크면 255로 맞추라고 할 수 있다.

S = np.clip(S * saturatuonScale, 0, 255)

# 나눈 채널을 하나로 합치는 함수 
hsvImage = cv2.merge( [ H, S, V ] )

# 위에서 float으로 작업을 했으므로, 다시 uint8로 변경해줘야 한다.
# hsvImage = hsvImage.astype(uint8)
hsvImage = np.uint8(hsvImage)

# BGR로 다시 변경해야, 우리가 눈으로 확인 가능
imgBgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)

cv2.imshow("cvt bgr", imgBgr)

cv2.waitKey()
cv2.destroyAllWindows()

