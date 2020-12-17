import os.path
import cv2
import numpy as np


kernel = np.ones((5, 5), np.uint8)



def function_dilated():



    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # DILATED CHESHIRE
        image_cheshire = cv2.imread('Cheshire.png')
        dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_cheshire.png',dilated_cheshire)
        print("Your image is now dilated and you add it in a file\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")




    print("----------FOR SHIBA----------")
    if os.path.isfile('chien.jpg'):
        print("File exist")
        # BLACK AND WHITE SHIBA
        image_shiba = cv2.imread('chien.jpg')
        # DILATED
        dilated_dog = cv2.dilate(image_shiba, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_dog.png',dilated_dog)
        print("Your image is now dilated and you add it in a file\n")
    else:
        print("File doesn't exist")



    print("----------FOR GRUMPY CAT----------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        # DILATED GRUMPY CAT
        dilated_grumpy_cat = cv2.dilate(image_grumpy_cat, kernel, iterations=1)
        cv2.imwrite(
            'filesystem_gray_picture/dilated_grumpy_cat.png',dilated_grumpy_cat)
        print("Your image is now dilated and you add it in a file\n\n\n\n")
    else:
        print("File doesn't exist")
