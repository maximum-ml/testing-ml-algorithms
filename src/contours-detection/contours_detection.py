import cv2
import numpy as np
import matplotlib.pyplot as plt

# https://medium.com/analytics-vidhya/how-to-detect-tables-in-images-using-opencv-and-python-6a0f15e560c3

# file = r’table.jpg’
file = 'input/2021.08.09_macbook_adapter.jpg'
im1 = cv2.imread(file, 0)
im2 = cv2.imread(file)

ret,thresh_value = cv2.threshold(im1,240,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)
plt.imshow(dilated_value)

contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]

cordinates = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cordinates.append((x, y, w, h))
    # bounding the images
    # if y < 50:
    cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 0, 255), 2)


plt.imshow(im2)
cv2.namedWindow('detecttable', cv2.WINDOW_NORMAL)
# cv2.imwrite('detecttable.jpg', im2)
