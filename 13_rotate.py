import cv2

source = cv2.imread('data/images/sample.jpg', 1)

# 회전의 중심 좌표.
center = (source.shape[1]/2, source.shape[0]/2)
rotationAngle=90
scaleFactor = 1

rotationMatrix = cv2.getRotationMatrix2D( center, rotationAngle, scaleFactor)

print(rotationMatrix)

result = cv2.warpAffine(source, rotationMatrix,
                        (source.shape[1], source.shape[0]))

cv2.imshow("Original", source)
cv2.imshow("Rotated Image", result)
cv2.waitKey()
cv2.destroyAllWindows()