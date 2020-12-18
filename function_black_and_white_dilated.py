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
