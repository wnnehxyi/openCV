import cv2
import numpy as np

datapath = "D:/.../_opencv_pictures/"

"""  
# read pictures 
img = cv2.imread(datapath+"one.jpg")


# rescale picture size 
img = cv2.resize(img, (600,400)) #pixels

# The image height and width become 0.5 times
img = cv2.resize(img, (0,0), fx=0.5, fy = 0.5)


cv2.imshow("one",img)
cv2.waitKey(0)  # 0:unlimited # display a window for given milliseconds or until any key is pressed.
"""

"""
# read videos
#cap = cv2.VideoCapture(datapath+"try.mp4")

# capture footage
cap = cv2.VideoCapture(0) #0:laptop lens #1:external lens

while True:
    ret, frame = cap.read()  #ret: whether the image fetch was successful  #frame: the next frame picture
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    if ret:
        cv2.imshow("video", frame)
    else:
        break
    if cv2.waitKey(10) == ord("q"):  #10: adjust the video speed  #press"q" : close the video
        break
"""


# make your own pictures
img_self = np.empty((300,300,3), np.uint8)  #0~255 →2^8 →8bits。uint: natural number


img = cv2.imread(datapath+"one.jpg")
img = cv2.resize(img, (0,0), fx=0.3, fy = 0.3)

"""
#  modify the first 300 pixels color
for i in range(300):
    for j in range(300):
        img[i][j] = [0,255,0]  # B,G,R

cv2.imshow("img",img)
cv2.waitKey(0)
"""

# cut pictures
newImg = img[:150, :200]

cv2.imshow("img_small",newImg)
cv2.waitKey(0)



