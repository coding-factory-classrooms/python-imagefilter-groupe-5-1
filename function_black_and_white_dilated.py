import os.path
import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)


def function_black_and_white_dilated():
    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # BLACK AND WHITE CHESHIRE
        image_cheshire = cv2.imread('Cheshire.png')
        image_gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/Cheshire_gray.png', image_gray_cheshire)
        print("Your image is now in black and white and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
        if os.path.isfile('filesystem_gray_picture/Cheshire_gray.png'):
            print("File exist")
            # DILATED CHESHIRE
            image_cheshire = cv2.imread('filesystem_gray_picture/Cheshire_gray.png')
            dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
            cv2.imwrite('filesystem_gray_picture/black_and_white_dilated_cheshire.png', dilated_cheshire)
            print("Your image is now dilated and black and white\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")

    print("----------FOR SHIBA----------")
    if os.path.isfile('chien.jpg'):
        print("File exist")
        # BLACK AND WHITE SHIBA
        image_shiba = cv2.imread('chien.jpg')
        image_gray_shiba = cv2.cvtColor(image_shiba, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/shiba_gray.jpg', image_gray_shiba)
        print("Your image is now in black and white and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
        if os.path.isfile('filesystem_gray_picture/shiba_gray.jpg'):
            print("File exist")
            # DILATED SHIBA
            image_shiba = cv2.imread('filesystem_gray_picture/shiba_gray.jpg')
            dilated_shiba = cv2.dilate(image_shiba, kernel, iterations=1)
            cv2.imwrite('filesystem_gray_picture/black_and_white_dilated_shiba.jpg', dilated_shiba)
            print("Your image is now dilated and black and white\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")

    print("----------FOR GRUMPY CAT---------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        # BLACK AND WHITE GRUMPY CAT
        image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        image_gray_grumpy_cat = cv2.cvtColor(image_grumpy_cat, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/grumpy_cat_gray.jpg', image_gray_grumpy_cat)
        print("Your image is now in black and white and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
        if os.path.isfile('filesystem_gray_picture/grumpy_cat_gray.jpg'):
            print("File exist")
            # DILATED GRUMPY CAT
            image_grumpy_cat = cv2.imread('filesystem_gray_picture/grumpy_cat_gray.jpg')
            dilated_grumpy_cat = cv2.dilate(image_grumpy_cat, kernel, iterations=1)
            cv2.imwrite('filesystem_gray_picture/black_and_white_dilated_grumpy_cat.jpg', dilated_grumpy_cat)
            print("Your image is now dilated and black and white\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")
