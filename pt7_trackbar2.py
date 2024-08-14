import numpy as np
import cv2 as cv

def nothing(x):
    print(x)


cv.namedWindow('image1')

cv.createTrackbar('CP','image1',10,400,nothing)

switch = 'color or gray'
cv.createTrackbar(switch, 'image1',0,1,nothing)

while(1):
    img=cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP','image1')
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img,str(pos),(50,130),font,2,(0,0,255),4)

    k=cv.waitKey(1)
    if k ==27:
        break

    
    s = cv.getTrackbarPos(switch,'image1')

    if s ==0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    
    img=cv.imshow('image1',img)

    

cv.destroyAllWindows()    