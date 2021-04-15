import cv2

imageName = "data/images/opening.png"

image = cv2.imread(imageName, 0)

cv2.imshow("original", image)

openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                    (2*openingSize+1, 2*openingSize+1) )

imageOpend = cv2.morphologyEx(image, cv2.MORPH_OPEN, element, iterations=3)

cv2.imshow("opened", imageOpend)

cv2.waitKey()
cv2.destroyAllWindows()