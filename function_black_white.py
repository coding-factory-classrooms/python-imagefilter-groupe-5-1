import os.path
import cv2



def function_black_and_white():



    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # BLACK AND WHITE CHESHIRE
        image_cheshire = cv2.imread('Cheshire.png')
        image_gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/Cheshire_gray.png',image_gray_cheshire)
        print("Your image is now in black and white and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")




    print("----------FOR SHIBA----------")
    if os.path.isfile('chien.jpg'):
        print("File exist")
        # BLACK AND WHITE SHIBA
        image_shiba = cv2.imread('chien.jpg')
        image_gray_shiba = cv2.cvtColor(image_shiba, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/shiba_gray.png',image_gray_shiba)
        print("Your image is now in black and white and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")




    print("----------FOR GRUMPY CAT----------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        # BLACK AND WHITE GRUMPY CAT
        image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        image_gray_grumpy_cat = cv2.cvtColor(image_grumpy_cat, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('filesystem_gray_picture/gray_grumpy_cat.jpg',image_gray_grumpy_cat)
        print("Your image is now in black and white and you add it in a filesystem\n\n\n\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
