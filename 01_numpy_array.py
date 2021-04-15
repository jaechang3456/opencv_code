import cv2

imageName = "data/images/sample.jpg"

# opencv 로 이미지 열기
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크
if image is None :
    print("이미지 열수 없다.")

print(image)

print(image.shape)

# Gray Scale Image : 1개의 행렬로 만들고, 0~255까지의 숫자로 채워진
# 행렬로 변환한 이미지

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

cv2.imshow("image", image)
cv2.imshow("Gray Scale", grayImage)

# 위의 이미지를 화면애 표시하는 코드는, 실행되었다가 종료된다.
# 왜냐하면, 이 파일 자체를 cpu가 실행해서 끝냈기 때문에
# 위의 imshow 함수는 바로 종료가 된다.
# 따라서 위의 imshow 함수를 실행시켜, 눈으로 확인하기 위해서는
# 다음처럼 코드를 작성해야 한다.

cv2.waitKey(0)
cv2.destroyAllWindows()