import numpy as np
import cv2

#img= cv2.imread('lena.jpg',1)
img= np.zeros([600,1000,3],np.uint8)
#img=cv2.line(img,(0,0),(255,255),(0,0,90),5)
#img=cv2.arrowedLine(img,(0,80),(45,255),(0,260,90),10)
img=cv2.rectangle(img,(50,80),(89,35),(60,0,0),10)
img=cv2.rectangle(img,(50,80),(89,35),(0,240,0),-1)
font = cv2.FONT_HERSHEY_DUPLEX
font2 = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img,'kirTi', (60,200),font,5,(100,160,160),7,cv2.LINE_AA)
img = cv2.putText(img,'cutie pie', (80,400),font2,5,(256,280,0),4,cv2.LINE_AA)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
