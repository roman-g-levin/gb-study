#pip install opencv-python

import cv2
# cv2 работает в формате BGR! (не RGB!)

img = cv2.imread('test.jpg')

print(img.shape)
img = cv2.resize(img, (500, 500))
print(img.shape)

cv2.imshow('Result', img)
cv2.waitKey(0)