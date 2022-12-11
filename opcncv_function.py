import cv2
import numpy as np

datapath = "D:/.../_opencv_pictures/"
data_save = "D:/.../_opencv_pictures_save/"

img = cv2.imread(datapath+"one.jpg")
img = cv2.resize(img, (0,0), fx=0.3, fy = 0.3)

# convert color pictures to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the picture
img_blur = cv2.GaussianBlur(img, (7,7),0) # (kernel size: must be odd numbers, std)

# get image edge 
# edge pixel values ​​are often very different from surrounding pixel values
# canny: calculate the difference score of pixel value and its surrounding pixel values.
img_edge = cv2.Canny(img,150,200) #(img, minimum threshold, maximum threshold)

# get the thicker image edges thicker
kernel = np.ones((3,3), np.uint8)
img_dila = cv2.dilate(img_edge, kernel, iterations=1)

# get the thicker image edges thinner
img_eros = cv2.erode(img_dila, kernel, iterations=1)

cv2.imshow("one",img)
cv2.imshow("gray",img_gray)
cv2.imshow("blur",img_blur)
cv2.imshow("edge",img_edge)
cv2.imshow("dila",img_dila)
cv2.imshow("eros",img_eros)

cv2.imwrite(data_save+"one_gray.png",img_gray)
cv2.imwrite(data_save+"one_blur.png",img_blur)
cv2.imwrite(data_save+"one_edge.png",img_edge)
cv2.imwrite(data_save+"one_dila.png",img_dila)
cv2.imwrite(data_save+"one_eros.png",img_eros)
cv2.waitKey(0)  # 0:unlimited