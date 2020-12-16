
import cv2
import numpy as np


def function_dilated():

    kernel = np.ones((5, 5), np.uint8)

    image_cheshire = cv2.imread('Cheshire.png')
    dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
    cv2.imwrite('dilated_cheshire.png', dilated_cheshire)

    image_shiba = cv2.imread('chien.jpg')
    dilated_dog = cv2.dilate(image_shiba, kernel, iterations=1)
    cv2.imwrite('dilated_dog.png', dilated_dog)

    image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
    dilated_grumpy_cat = cv2.dilate(image_grumpy_cat, kernel, iterations=1)
    cv2.imwrite('dilated_grumpy_cat.png', dilated_grumpy_cat)

    print("Your image is now in dilated and you add it in a filesystem\n")
