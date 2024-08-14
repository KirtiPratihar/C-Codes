import cv2
import datetime
cap=cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,400)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame= cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_DUPLEX
        text="width:"+str(cap.get(3))+"height:"+str(cap.get(4))
        dt=str(datetime.datetime.now())
        frame= cv2.putText(frame,dt,(10,60),font,1,(110,0,200),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1)== ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()          