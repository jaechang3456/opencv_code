import cv2
import numpy as np

def mouse_handler(event, x, y, flags, data) :

    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y), 3, (0, 0, 255), 5, 16)
        cv2.imshow( "Image", data['im'] )
        if len(data['points']) < 4 :
            data['points'].append([x,y])

def get_four_points(im) :
    data = {}
    data['im'] = im.copy()
    data['points'] = []

    cv2.imshow("Image", im)
    cv2.setMouseCallback("Image", mouse_handler, data)
    cv2.waitKey(0)

    # 유저가 마우스로 찍은 점을 float으로 바꿔줘야 한다.
    points = np.array(data['points'], dtype=float)
    return points
