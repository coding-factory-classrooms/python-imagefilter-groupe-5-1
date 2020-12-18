import os.path
import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)


def function_all():
    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # DILATED CHESHIRE
        image_cheshire = cv2.imread('Cheshire.png')
        dilated_cheshire = cv2.dilate(image_cheshire, kernel, iterations=1)
        cv2.imwrite('filesystem_gray_picture/dilated_cheshire0.png', dilated_cheshire)
        print("Your image is now dilated and you add it in a file\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
        if os.path.isfile('filesystem_gray_picture/dilated_cheshire0.png'):
            print("File exist")
            # BLURRY CHESHIRE
            image_blurry_cheshire = cv2.imread('filesystem_gray_picture/dilated_cheshire0.png')
            src = cv2.imread('filesystem_gray_picture/dilated_cheshire0.png', cv2.IMREAD_UNCHANGED)
            image_blurry_cheshire = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/dilated_blurry_cheshire0.png', image_blurry_cheshire)
            print("Your image is now in blurry and dilated\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")
            if os.path.isfile('filesystem_gray_picture/dilated_blurry_cheshire0.png'):
                print("File exist")
                # BLACK AND WHITE CHESHIRE
                image_cheshire = cv2.imread('filesystem_gray_picture/dilated_blurry_cheshire0.png')
                image_gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('filesystem_gray_picture/Cheshire_all.png', image_gray_cheshire)
                print("Your image is now in blurry and dilated and in black and white\n")
                cv2.waitKey(0)
            else:
                print("File doesn't exist")