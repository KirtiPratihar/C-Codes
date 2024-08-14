import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('image1')

cv.createTrackbar('B','image1',0,255,nothing)
cv.createTrackbar('G','image1',0,255,nothing)
cv.createTrackbar('R','image1',0,255,nothing)

switch = '0 :OFF\n 1:ON'
cv.createTrackbar(switch, 'image1',0,1,nothing)

while(1):
    cv.imshow('image1',img)
    k=cv.waitKey(1)
    if k ==27:
        break

    b = cv.getTrackbarPos('B','image1')
    g = cv.getTrackbarPos('G',"image1")
    r = cv.getTrackbarPos('R','image1')
    s = cv.getTrackbarPos(switch,'image1')

    if s ==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()    