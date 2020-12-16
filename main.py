import os.path
import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

print("----------FOR CHESHIRE----------")
if os.path.isfile('Cheshire.png'):
    print("File exist")
    # BLACK AND WHITE
    image_cheshire = cv2.imread('Cheshire.png')
    image_gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Cheshire_gray.png', image_gray_cheshire)
    print("Your image is now in black and white and you add it in a filesystem")
    # DILATED
    image_cheshire = cv2.imread('Cheshire.png')
    dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
    cv2.imwrite('dilated_cheshire.png', dilated_cheshire)
    print("Your image is now dilated and you add it in a file\n")
    cv2.waitKey(0)
else:
    print("File doesn't exist")

print("----------FOR SHIBA----------")
if os.path.isfile('chien.jpg'):
    print("File exist")
    # BLACK AND WHITE
    image_shiba = cv2.imread('chien.jpg')
    image_gray_shiba = cv2.cvtColor(image_shiba, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('shiba_gray.png', image_gray_shiba)
    print("Your image is now in black and white and you add it in a filesystem")
    cv2.waitKey(0)
    # DILATED
    dilated_dog = cv2.dilate(image_shiba, kernel, iterations=1)
    cv2.imwrite('dilated_dog.png', dilated_dog)
    print("Your image is now dilated and you add it in a file\n")
else:
    print("File doesn't exist")

print("----------FOR GRUMPY CAT----------")
if os.path.isfile('grumpy_cat_project.jpg'):
    print("File exist")
    # BLACK AND WHITE
    image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
    image_gray_grumpy_cat = cv2.cvtColor(image_grumpy_cat, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_grumpy_cat.jpg', image_gray_grumpy_cat)
    print("Your image is now in black and white and you add it in a filesystem")
    cv2.waitKey(0)
    # DILATED
    dilated_grumpy_cat = cv2.dilate(image_grumpy_cat, kernel, iterations=1)
    cv2.imwrite('dilated_grumpy_cat.png', dilated_grumpy_cat)
    print("Your image is now dilated and you add it in a file\n")
else:
    print("File doesn't exist")







