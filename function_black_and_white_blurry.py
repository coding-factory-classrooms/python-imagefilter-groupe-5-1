import cv2
import os.path


def function_black_and_white_blurry():
    """
    She check if the image exist.
    The image became a value and we put the gray filter.
    Then the program take the new image with the gray filter on and add the blurry filter.
    She do that for the 3 images.
    """
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
            # BLURRY CHESHIRE
            image_blurry_cheshire = cv2.imread('filesystem_gray_picture/Cheshire_gray.png')
            src = cv2.imread('filesystem_gray_picture/Cheshire_gray.png', cv2.IMREAD_UNCHANGED)
            image_blurry_cheshire = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/black_and_white_blurry_cheshire.png', image_blurry_cheshire)
            print("Your image is now in blurry and black and white\n")
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
            # BLURRY SHIBA
            image_blurry_shiba = cv2.imread('filesystem_gray_picture/shiba_gray.jpg')
            src = cv2.imread('filesystem_gray_picture/shiba_gray.jpg', cv2.IMREAD_UNCHANGED)
            image_blurry_shiba = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/black_and_white_blurry_shiba.jpg', image_blurry_shiba)
            print("Your image is now in blurry and black and white\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")
            
    print("----------FOR GRUMPY CAT----------")
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
            # BLURRY GRUMPY CAT
            image_blurry_grumpy_cat = cv2.imread('filesystem_gray_picture/grumpy_cat_gray.jpg')
            src = cv2.imread('filesystem_gray_picture/grumpy_cat_gray.jpg', cv2.IMREAD_UNCHANGED)
            image_blurry_grumpy_cat = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite('filesystem_gray_picture/black_and_white_blurry_grumpy_cat.jpg', image_blurry_grumpy_cat)
            print("Your image is now in blurry and black and white\n")
            cv2.waitKey(0)
        else:
            print("File doesn't exist")
