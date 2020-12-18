import os.path
import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)


def function_blurry_dilated():
    """
    She check if the image exist.
    The image became a value and we put the blurry filter.
    Then the program take the new image with the filter on and add the dilated filter.
    Same for the 3 images.
    """
    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # DILATED CHESHIRE
        image_cheshire = cv2.imread('Cheshire.png')
        dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_cheshire.png', dilated_cheshire)
        print("Your image is now dilated and you add it in a file\n")
        cv2.waitKey(0)
        if os.path.isfile('filesystem_gray_picture/dilated_cheshire.png'):
            print("File exist")
            # BLURRY CHESHIRE
            image_blurry_cheshire = cv2.imread('Cfilesystem_gray_picture/dilated_cheshire.png')
            src = cv2.imread('filesystem_gray_picture/dilated_cheshire.png', cv2.IMREAD_UNCHANGED)
            image_blurry_cheshire = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/blurry_dilated_cheshire.png', image_blurry_cheshire)
            print("Your image is now in blurry and dilated\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")

    print("----------FOR SHIBA----------")
    if os.path.isfile('chien.jpg'):
        print("File exist")
        # DILATED SHIBA
        image_shiba = cv2.imread('chien.jpg')
        dilated_shiba = cv2.dilate(image_shiba, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_shiba.jpg', dilated_shiba)
        print("Your image is now dilated and you add it in a file\n")
        cv2.waitKey(0)
        if os.path.isfile('filesystem_gray_picture/dilated_shiba.jpg'):
            print("File exist")
            # BLURRY SHIBA
            image_blurry_shiba = cv2.imread('Cfilesystem_gray_picture/dilated_shiba.jpg')
            src = cv2.imread('filesystem_gray_picture/dilated_shiba.jpg', cv2.IMREAD_UNCHANGED)
            image_blurry_shiba = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/blurry_dilated_shiba.png', image_blurry_shiba)
            print("Your image is now in blurry and dilated\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")

    print("----------FOR GRUMPY CAT----------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        # DILATED GRUMPY CAT
        image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        dilated_grumpy_cat = cv2.dilate(image_grumpy_cat, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_grumpy_cat.jpg', dilated_grumpy_cat)
        print("Your image is now dilated and you add it in a file\n")
        cv2.waitKey(0)
        if os.path.isfile('filesystem_gray_picture/dilated_grumpy_cat.jpg'):
            print("File exist")
            # BLURRY GRUMPY CAT
            image_blurry_grumpy_cat = cv2.imread('Cfilesystem_gray_picture/dilated_grumpy_cat.jpg')
            src = cv2.imread('filesystem_gray_picture/dilated_grumpy_cat.jpg', cv2.IMREAD_UNCHANGED)
            image_blurry_shiba = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/blurry_dilated_grumpy_cat.png', image_blurry_grumpy_cat)
            print("Your image is now in blurry and dilated\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")
