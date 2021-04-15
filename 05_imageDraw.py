import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)

# 선 그리기
imageLine = image.copy()

cv2.line(imageLine, (322,179), (400,183), (255,0,0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('image line', imageLine)

# 원그리기
imageCircle = image.copy()

cv2.circle(imageCircle, (350,200),150,(255,0,0),thickness=3,lineType=cv2.LINE_AA)
# cv2.imshow('image circle', imageCircle)

# 타원그리기
imageEllipse = image.copy()

cv2.ellipse(imageEllipse, (360,200),(100,170),45,0,360,(0,255,0), thickness=2)
cv2.ellipse(imageEllipse, (360,200),(100,170),135,0,360,(0,0,255), thickness=2)

# cv2.imshow('ellips',imageEllipse)

# 사각형 그리기
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208,55), (450,355), (255,0,0), thickness=3)
# cv2.imshow("rectangle", imageRectangle)

# 글자 넣기
imageText = image.copy()
cv2.putText(imageText, "Mark Zuckerberg", (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2 )
# cv2.imshow("Text", imageText)

imageRectangleText = image.copy()
cv2.rectangle(imageRectangleText, (208,55), (450,355), (255,0,0), thickness=3)
cv2.putText(imageRectangleText, "Mark Zuckerberg", (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2 )
cv2.imshow("RectangleText", imageRectangleText)

cv2.waitKey(0)
cv2.destroyAllWindows()