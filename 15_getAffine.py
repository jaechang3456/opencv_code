import cv2
import numpy as np

input_tri = np.float32( [ 50,50,100,100,200,150 ] )
# 삼각형 세 점의 좌표로 변환
input_tri = input_tri.reshape(3,2)

# 변환된 이미지의 세 2점이 좌표
output_tri = np.float32 ( [ 70,76,142,101,272,136 ] )
# 세점의 좌표로 변환
output_tri = output_tri.reshape(3,2)

print(input_tri)
print(output_tri)

warpMat = cv2.getAffineTransform(input_tri, output_tri)

print(warpMat)