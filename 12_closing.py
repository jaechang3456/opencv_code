import cv2

imageName = "data/images/closing.png"

image = cv2.imread(imageName, 0)

cv2.imshow("original", image)

openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                    (2*openingSize+1, 2*openingSize+1) )

imageOpend = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element, iterations=5)

cv2.imshow("closed", imageOpend)

cv2.waitKey()
cv2.destroyAllWindows()