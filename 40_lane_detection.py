import cv2
import numpy as np

# # 1. 이미지 가져오기
# image = cv2.imread('data3/test_image.jpg')

# cv2.imshow('ori', image)

# # 2. 그레이스케일로 변경
# lanelines_image = image.copy()

# gray_conversion = cv2.cvtColor(lanelines_image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray', gray_conversion)

# # 3. smoothing
# blur_conversion = cv2.GaussianBlur(gray_conversion, (5,5), 0)

# cv2.imshow('smooth', blur_conversion)

# # 4. Canny Edge Detection
# canny_conversion = cv2.Canny(blur_conversion, 50, 155)

# cv2.imshow('canny', canny_conversion)

# 5. Masking the region of interest (ROI) 함수로 만들기

def reg_of_interest(image) :
    image_height = image.shape[0]
    polygons = np.array( [[ (200, image_height) , (1100, image_height), (550, 250) ]] )
    image_mask = np.zeros_like(image)
    cv2.fillPoly(image_mask, polygons, 255)
    masking_image = cv2.bitwise_and(image, image_mask)
    return masking_image

# 6. 케니에지 처리하는 부분도 함수로 만들자.

def canny_edge(image) :
    gray_conversion = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_conversion = cv2.GaussianBlur(gray_conversion, (5,5), 0)
    canny_conversion = cv2.Canny(blur_conversion, 50, 150)
    return canny_conversion

def show_lines(image, lines) : 
    lines_image = np.zeros_like(image)
    if lines is not None :
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i]:
                cv2.line(lines_image,(x1,y1),(x2,y2),(255,0,0), 10 )
    return lines_image

# 여러 선을, 하나의 선으로 만들어 주는 함수.
# 방법은? 기울기와 y절편을 평균으로 해서 하나의 기울기와 y절편을 갖도록 만드는 방법.
def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1- intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        # 직선의 기울기와 y절편을 가져올 수 있다.
        parameter = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameter[0]
        intercept = parameter[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average =np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis =0)
    left_line =make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)

    return np.array([[left_line, right_line]])


image = cv2.imread('data3/test_image.jpg')
lanelines_image = image.copy()

canny_conversion = canny_edge(lanelines_image)
roi_conversion = reg_of_interest(canny_conversion)

lines = cv2.HoughLinesP(roi_conversion, 1, np.pi/180, 100, minLineLength = 40, maxLineGap = 5)

averaged_lines = average_slope_intercept(lanelines_image, lines)

lines_image = show_lines(lanelines_image, averaged_lines)

combine_image = cv2.addWeighted(lanelines_image, 0.8, lines_image, 1, 1)

# cv2.imshow('ori', lanelines_image)
# cv2.imshow("roi", lines_image)
# cv2.imshow("combined", combine_image)


cap = cv2.VideoCapture('data3/test2.mp4')
while cap.isOpened() :
    ret, frame = cap.read()
    canny_image = canny_edge(frame)
    roi_image = reg_of_interest(canny_image)
    lines = cv2.HoughLinesP(roi_image, 1, np.pi / 180, 100, minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = show_lines(frame, averaged_lines)
    combine_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow('result', combine_image)
    if cv2.waitKey(25) & 0xFF == 27 :
        break
    
cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()