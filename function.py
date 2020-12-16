import cv2
import numpy as np

cheshire = cv2.imread('Cheshire.png', 0)
grumpy_cat = cv2.imread('grumpy_cat_project.jpg', 0)
chien = cv2.imread('chien.jpg', 0)
kernel = np.ones((5, 5), np.uint8)


def dilated_picture():
    dilation = cv2.dilate(chien, kernel, iterations=1)
    cv2.imshow('Dilated dog', dilation)
    # cv2.waitKey(0)

    dilation = cv2.dilate(cheshire, kernel, iterations=1)
    cv2.imshow('Dilated cheshire', dilation)
    # cv2.waitKey(0)

    dilation = cv2.dilate(grumpy_cat, kernel, iterations=1)
    cv2.imshow('Dilated grumpy cat', dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
