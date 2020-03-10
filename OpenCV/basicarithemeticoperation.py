#ROI = region of intrest

import  cv2
import numpy as np

img = cv2.imread('messi5.jpg',1)
img2 = cv2.imread('opencv-logo.png',1)
print(img.shape) #return tuple and no rows,colouns
print(img.size) #returns no of pixel
print(img.dtype)#returns image data type obtained
b,g,r =cv2.split(img)
img =cv2.merge((b,g,r))
ball=img[280:340 ,330:390]
img[273:333,100:160] = ball #COPY BALL
#resize the image
img = cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
#add the image and image should be of same sizw to add the image so it is resized
# dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,.9,img2,0.3,0) #0.9,0.5=opacity,0=gamma scale
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()