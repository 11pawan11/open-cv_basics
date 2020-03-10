import numpy as np 
import cv2
img =np.zeros([512,512,3],np.uint8)
# img =cv2.imread('messi5.jpg',1)
# img =cv2.line(img,(0,0),(255,255),(255,0,0),2)
# img =cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),2)

img =cv2.rectangle(img,(250,40),(410,200),(0,255,2),1)
img =cv2.circle(img,(200,63),63,(0,255,2),1)
font =cv2.FONT_HERSHEY_SIMPLEX
img =cv2.putText(img,'OpenCv',(90,85),font,4,(255,255,255),1,cv2.LINE_AA)


cv2.imshow('messi5',img)
if cv2.waitKey(0) & 0xFF== ord('q'):
    cv2.destroyAllWindows()