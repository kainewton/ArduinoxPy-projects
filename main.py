import cv2
from cycler import K
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8,maxHands=2)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        print(fingerUp)
        
        cnt.led(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8)    
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_ITALIC,1,(255,255,255),1,cv2.LINE_8) 

    cv2.imshow("LED Controller",frame)
    f=cv2.waitKey(1)
    if f==ord("f"):
        break

cap.release()
cv2.destroyAllWindows()


