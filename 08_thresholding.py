import cv2

src = cv2.imread('data/images/threshold.png', 0)

# 구분하기 위한 값 설정
thresh = 0
# 위에서 설정한 값보다 큰 것들은, 모두 255로 색을 변경하겠다는 뜻
maxValue = 255

cv2.imshow("Original", src)

# 두번째 리턴값이, 적용된 이미지(numpy)
th,dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow("Thresholded Image", dst)


cv2.waitKey()
cv2.destroyAllWindows()