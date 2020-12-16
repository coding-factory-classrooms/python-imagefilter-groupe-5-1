
import cv2
import os.path



def blurry():


    print("----------FOR CHESHIRE----------")
    if os.path.isfile('Cheshire.png'):
        print("File exist")
        # BLURRY CHESHIRE
        blurry_grumpy_cat = cv2.imread('Cheshire.png')
        src = cv2.imread('Cheshire.png', cv2.IMREAD_UNCHANGED)
        blurry_grumpy_cat = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/burry_cheshire.png',blurry_grumpy_cat)
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
        cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/shiba_blurry.png',image_blurry_shiba)
        print("Your image is now in blurry and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")



    print("----------FOR CHESHIRE----------")
    if os.path.isfile('grumpy_cat_project.jpg'):
        print("File exist")
        # BLURRY GRUMPY CAT
        blurry_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
        src = cv2.imread('grumpy_cat_project.jpg', cv2.IMREAD_UNCHANGED)
        blurry_grumpy_cat = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
        cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/blurry_grumpy_cat.png',blurry_grumpy_cat)
        print("Your image is now in blurry and you add it in a filesystem\n")
        cv2.waitKey(0)
    else:
        print("File doesn't exist")
