import numpy as np
import cv2
 
# this is how we search files module in python
# events =[i for i in dir(cv2) if 'EVENT' in i]
# print events

def event_click(event, x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDOWN:
         blue =  img[y,x,0]
         green = img[y,x,1]
         red = img[y,x,2]
         cv2.circle(img, (x,y) ,3, (0,255,0),-1)
         myimage=np.zeros((512,512,3),np.uint8)
         myimage[:] = [blue,green,red] #to create the second window
         cv2.imshow('image',myimage)



    #     cv2.circle(img,(x,y),3,(0,255,0),-1)
    #     points.append((x,y))
    #     if len(points)>=2: #if click is more than 2 then add the points with line
    #         cv2.line(img,points[-1],points[-2],(255,0,0),5) 
    #     cv2.imshow('image',img)

# img = np.zeros((512,512,3),np.uint8) #create black image    
img =cv2.imread('messi5.jpg',1) 
cv2.imshow('image',img)  
points =[]
cv2.setMouseCallback('image',event_click)
cv2.waitKey(0) 
cv2.destroyAllWindows()

