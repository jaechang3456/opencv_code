import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 

#칼라 이미지.
image_color = cv2.imread('data2/image.jpg')
# cv2.imshow("color",image_color)

# 우리가 필요한건 그레이 스케일 
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",image_gray)

image_copy = image_gray.copy()

# 값이 195 미만인 것들은, 0으로 셋팅.
print(image_color.shape)
print(image_copy.shape)

print(image_copy[ : , : ] < 195)

image_copy[image_copy[ : , : ] < 195 ] = 0

# cv2.imshow('copy', image_copy)

image = cv2.imread('data2/test_image.jpg')
print('Height = ' , int(image.shape[0]), 'pixels')
print('Width = ' , int(image.shape[1]), 'pixels')

# cv2.imshow('Self Driving Car!', image)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('SDC Gray', gray_img)

# HSV 칼라 스페이스로 변경
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', hsv_image)

# Hue 채널만 표시 !
H, S, V = cv2.split(hsv_image)
# H = hsv_image[ : , : , 0 ]

# cv2.imshow("Hue", H)

sharp_kernel_1 = np.array( [ 
    [ 0, -1, 0],
    [-1, 5, -1],
    [ 0, -1, 0],
 ] )

sharpened_img_1 = cv2.filter2D(gray_img, -1, sharp_kernel_1)

# cv2.imshow("Gray", gray_img)
# cv2.imshow("Sharpen", sharpened_img_1)

sharp_kernel_2 = np.array( [ 
    [ 0, -1, 0],
    [-1, 9, -1],
    [ 0, -1, 0],
 ] )

sharpened_img_2 = cv2.filter2D(gray_img, -1, sharp_kernel_2)

# cv2.imshow("Sharpen", sharpened_img_2)

# Blurring
blur_img = cv2.GaussianBlur(gray_img, (5,5), 1)
# cv2.imshow("blur", blur_img)

# Sobel 이용한 edge detection
x_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=7)
# cv2.imshow('sobel x', x_sobel)

y_sobel = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=7)
# cv2.imshow('sobel y', y_sobel)

# 라플라시안은 한번에 수직수평 다 잡는다.
laplacian = cv2.Laplacian(gray_img, cv2.CV_64F)
# cv2.imshow("lapl", laplacian)

# Canny edge detection
threshold_1 = 120
threshold_2 = 200

canny_img = cv2.Canny(gray_img, threshold_1, threshold_2)
# cv2.imshow("canny", canny_img)

# transformation
image = cv2.imread('data2/test_image2.jpg')
# cv2.imshow("ori", image)

print(image.shape)

M_rotation = cv2.getRotationMatrix2D( ( image.shape[1]/2, image.shape[0]/2), 90, 0.5 )

rotated_img = cv2.warpAffine(image, M_rotation, (image.shape[1], image.shape[0]))

# cv2.imshow('rotated', rotated_img)

image = cv2.imread('data2/test_image3.jpg')
# cv2.imshow('ori', image)

height = image.shape[0]
width = image.shape[1]

T_matrix = np.array( [ 
    [1, 0, 120],
    [0, 1, -150]
] , dtype='float32' )

print(T_matrix)

translation_img = cv2.warpAffine(image, T_matrix, (width, height))
# cv2.imshow('tran', translation_img)

# Resizing
resized_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('resize', resized_image)

# Region of interest masking
# RoI : 관심영역

image_color = cv2.imread('data2/test5.jpg')

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray", image_gray)

print(image_gray.shape)

# np.zeros 함수는 파라미터로, 몇행 몇열로 만들지 넣어줘야 한다.
# blank = np.zeros( (image_gray.shape[0], image_gray.shape[1]) )

blank = np.zeros_like(image_gray)

print(blank.shape)

ROI = np.array( [[ (0,400), (300,250), (450, 300), (640, 400 )]] , dtype=np.int32 )

mask = cv2.fillPoly(blank, ROI, 255)

print(mask)

masked_image = cv2.bitwise_and(image_gray, mask)

# cv2.imshow('masked', masked_image)

# hough transform

image_c = cv2.imread('data2/calendar.jpg')
image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

image_canny = cv2.Canny(image_g, 50, 200, apertureSize=3)

lines = cv2.HoughLines(image_canny, 1, np.pi / 180, 250)

for i in range(len(lines)) :
    for rho, theta in lines[i] :
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 -1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(image_c, (x1,y1), (x2,y2), (255,0,0), 2)

cv2.imshow('canny', image_c)


cv2.waitKey()
cv2.destroyAllWindows()