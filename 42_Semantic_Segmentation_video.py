import numpy as np
import argparse
import imutils
import time
import cv2
import os
import matplotlib.pyplot as plt

DEFAULT_FRAME = 1
SET_WIDTH = int(600)

sv = cv2.VideoCapture('data4/video/video.mp4')

# Enet 모델 가져오기.
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net')
# 색 정보도 가져온다.
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')
# 맨 마지막 따옴표 없애기
CV_ENET_SHAPE_IMG_COLORS = CV_ENET_SHAPE_IMG_COLORS[ : -2+1]

CV_ENET_SHAPE_IMG_COLORS = np.array([ np.array(color.split(',')).astype('int') for color in CV_ENET_SHAPE_IMG_COLORS ])

try :
    prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() else cv2.CAP_PROP_FRAME_COUNT
    total = sv.get(prop)
    print("[INFO] {} total frames in veideo.".format(total))
except :
    print("[INFO] could not determine number of frames in vedeo")
    total = -1

while True :
    grabbed, frame = sv.read()

    if grabbed == False :
        break   

    normalize_image = 1 / 255.0
    resize_image_shape = ( 1024, 512 )
    video_frame = imutils.resize(frame, width = SET_WIDTH)
    blob_img = cv2.dnn.blobFromImage(frame, normalize_image, resize_image_shape, 0, swapRB = True, crop=False)
    cv_enet_model.setInput(blob_img)
    # 모델이, 세그멘테이션 추론(예측)하는데 얼마나 걸렸는지 측정.
    start_time = time.time()
    cv_enet_model_output = cv_enet_model.forward()
    end_time = time.time()

    (classes_num, height, width) = cv_enet_model_output.shape[ 1 : 4 ]

    class_map = np.argmax(cv_enet_model_output[0], axis=0)

    mask_class_map = CV_ENET_SHAPE_IMG_COLORS[class_map]

    mask_class_map = cv2.resize(mask_class_map, (video_frame.shape[1], video_frame.shape[0]), interpolation = cv2.INTER_NEAREST)

    cv_enet_model_output = ((0.3 * video_frame) + (0.7 * mask_class_map)).astype('uint8')

    cv2.imshow("Frame", cv_enet_model_output)
        
    if cv2.waitKey(25) & 0xFF == 27 :
        break

sv.release()

cv2.destroyAllWindows()




