import cv2
import function


function.dilated_picture()

image_cheshire = cv2.imread('Cheshire.png')
image_shiba = cv2.imread('chien.jpg')
image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')

gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
gray_shiba = cv2.cvtColor(image_shiba, cv2.COLOR_BGR2GRAY)
gray_grumpy_cat = cv2.cvtColor(image_grumpy_cat, cv2.COLOR_BGR2GRAY)


image_cheshire = cv2.imread('Cheshire.png')
image_gray_cheshire = cv2.cvtColor(image_cheshire, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/Cheshire_gray.png', image_gray_cheshire)

image_shiba = cv2.imread('chien.jpg')
image_gray_shiba = cv2.cvtColor(image_shiba, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/shiba_gray.png', image_gray_shiba)

image_grumpy_cat = cv2.imread('grumpy_cat_project.jpg')
image_gray_grumpy_cat = cv2.cvtColor(image_grumpy_cat, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C:/Users/33663/Documents/Projet-Python-Robin/Python/filesystem_gray_picture/gray_grumpy_cat.jpg', image_gray_grumpy_cat)


cv2.waitKey(0)




