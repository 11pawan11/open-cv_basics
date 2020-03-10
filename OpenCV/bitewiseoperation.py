import cv2
import numpy as np
img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 =cv2.imread('image.Jpg')
img1 =cv2.resize(img1,(312,212))
img2 =cv2.resize(img2,(312,212))
bitAnd =cv2.bitwise_xor(img2,img1)
# bitAnd =cv2.bitwise_and(img2,img1)

cv2.imshow('bitwis',bitAnd)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2) 
cv2.waitKey(0)
cv2.destroyAllWindows()
