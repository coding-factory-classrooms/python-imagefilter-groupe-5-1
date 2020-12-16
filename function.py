import cv2
import numpy as np


def dilated_picture():
    cheshire = cv2.imread('Cheshire.png', 0)
    grumpy_cat = cv2.imread('grumpy_cat_project.jpg', 0)
    chien = cv2.imread('chien.jpg', 0)
    kernel = np.ones((5, 5), np.uint8)
    
    dilated_dog = cv2.dilate(chien, kernel, iterations=1)
    cv2.imwrite('dilated_dog.png', dilated_dog)
    cv2.imshow('Dilated dog', dilated_dog)
    print("Your image is now dilated and you add it in a file")

    dilated_cheshire = cv2.dilate(cheshire, kernel, iterations=1)
    cv2.imwrite('dilated_cheshire.png', dilated_cheshire)
    cv2.imshow('Dilated cheshire', dilated_cheshire)
    print("Your image is now dilated and you add it in a file")

    dilated_grumpy_cat = cv2.dilate(grumpy_cat, kernel, iterations=1)
    cv2.imwrite('dilated_grumpy_cat.png', dilated_grumpy_cat)
    cv2.imshow('Dilated grumpy cat', dilated_grumpy_cat)
    print("Your image is now dilated and you add it in a file")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
