import cv2
import numpy as np

# FPS : Frame Per Second : 1초당 몇장의 사진으로 구성되어 있냐

cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False :
    print('Error opening video stream or file')

else :
    # 반복문이 필요한 이유? 비디오는 여러사진으로 구성되어 있으니까
    while (cap.isOpened()) :
        # 사진을 1장씩 가져와서
        ret, frame = cap.read()

        # 제대로 가져왔으면 표시
        if ret == True :

            # 키보드에서 esc 누르면 exit 하라는것
            cv2.imshow("Frame", frame)
            
            if cv2.waitKey(25) & 0xFF == 27 :
                break

        else :
            break

    cap.release()

    cv2.destroyAllWindows()


    