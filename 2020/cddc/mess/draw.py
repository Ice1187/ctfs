import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)

img.fill(200)

cv2.line(img, (20, 22), (21, 83), (0, 0, 255), 2)
cv2.line(img, (20, 50), (55, 47), (0, 0, 255), 2)
cv2.line(img, (54, 20), (55, 82), (0, 0, 255), 2)
cv2.line(img, (82, 25), (81, 80), (0, 0, 255), 2)
cv2.line(img, (106, 54), (133, 54), (0, 0, 255), 2)
cv2.line(img, (155, 88), (156, 28), (0, 0, 255), 2)
cv2.line(img, (156, 28), (188, 83), (0, 0, 255), 2)
cv2.line(img, (188, 83), (186, 29), (0, 0, 255), 2)
cv2.line(img, (209, 33), (210, 83), (0, 0, 255), 2)
cv2.line(img, (210, 83), (243, 83), (0, 0, 255), 2)
cv2.line(img, (243, 83), (243, 31), (0, 0, 255), 2)
cv2.line(img, (266, 37), (266, 84), (0, 0, 255), 2)
cv2.line(img, (266, 84), (296, 85), (0, 0, 255), 2)
cv2.line(img, (312, 35), (312, 81), (0, 0, 255), 2)
cv2.line(img, (312, 81), (339, 80), (0, 0, 255), 2)
cv2.line(img, (359, 53), (370, 33), (0, 0, 255), 2)
cv2.line(img, (370, 33), (389, 55), (0, 0, 255), 2)
cv2.line(img, (395, 84), (424, 84), (0, 0, 255), 2)
cv2.line(img, (431, 53), (441, 30), (0, 0, 255), 2)
cv2.line(img, (441, 30), (460, 53), (0, 0, 255), 2)
cv2.line(img, (483, 20), (482, 67), (0, 0, 255), 2)
cv2.line(img, (483, 78), (483, 85), (0, 0, 255), 2)

cv2.imshow('My Image', img)
cv2.waitKey(0)
