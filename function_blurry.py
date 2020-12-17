import cv2
import os.path



def blurry():


    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # BLURRY CHESHIRE
        image_blurry_cheshire = cv2.imread('Cheshire.png')
        src = cv2.imread('Cheshire.png', cv2.IMREAD_UNCHANGED)
        image_blurry_cheshire = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        cv2.imwrite('filesystem_gray_picture/blurry_cheshire.png',image_blurry_cheshire)
        print("Your image is now in blurry and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")



    print("----------FOR SHIBA----------")
    if os.path.isfile('chien.jpg'):
        print("File exist")
        # BLURRY SHIBA
        image_blurry_shiba = cv2.imread('chien.jpg')
        src = cv2.imread('chien.jpg', cv2.IMREAD_UNCHANGED)
        image_blurry_shiba = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        cv2.imwrite('filesystem_gray_picture/shiba_blurry.png',image_blurry_shiba)
        print("Your image is now in blurry and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")



    print("----------FOR CHESHIRE----------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        # BLURRY GRUMPY CAT
        image_blurry_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        src = cv2.imread('grumpy_cat_project.jpg', cv2.IMREAD_UNCHANGED)
        image_blurry_grumpy_cat = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        cv2.imwrite('filesystem_gray_picture/blurry_grumpy_cat.png',image_blurry_grumpy_cat)
        print("Your image is now in blurry and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
