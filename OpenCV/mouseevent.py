import numpy as np
import cv2
 
# this is how we search files module in python
# events =[i for i in dir(cv2) if 'EVENT' in i]
# print events

def event_click(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font =cv2.FONT_HERSHEY_SIMPLEX
        StrXY=str(x) + ',' + str(y)
        cv2.putText(img,StrXY,(x,y),font,1,(0,0,255),2)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font =cv2.FONT_HERSHEY_SIMPLEX
        StrXYZ=str(blue) + ',' + str(green) +',' + str(red)
        cv2.putText(img,StrXYZ,(x,y),font,1,(0,255,0),2)
        cv2.imshow('image',img)
#img = np.zeros((512,512,3),np.uint8)      
#cv2.imshow('image',img)  
img =cv2.imread('messi5.jpg',1) 
cv2.imshow('image',img) 
cv2.setMouseCallback('image',event_click)
cv2.waitKey(0) 
cv2.destroyAllWindows()

