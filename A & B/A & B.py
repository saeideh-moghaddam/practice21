import cv2

image1 = cv2.imread ( "hw2/a.tif" , 0)
image2 = cv2.imread ( "hw2/b.tif" , 0)
image = image2 - image1 
cv2.imwrite("a & b.jpg" , image)
cv2.imshow("a - b",image)
cv2.waitKey()