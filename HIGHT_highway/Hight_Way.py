import cv2
import numpy as np

img = []

for i in range(15):
   photo = cv2.imread(f"HIGHT_WAY\highway\h{i}.jpg", 0)
   img.append(photo)

rows, cols = img[0].shape

new_photo = np.zeros((rows, cols), dtype='uint8')
for i in range(len(img)):
    new_photo += img[i] // len(img)

cv2.imwrite("Hight_way.jpg", new_photo)
cv2.imshow("Hight_way", new_photo)
cv2.waitKey()