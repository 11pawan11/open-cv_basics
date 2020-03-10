import cv2
#read the image
# cv2.imread('messi5.jpg',0)
img = cv2.imread('messi5.jpg',-1)
#img = cv2.imread('messi5.jpg',0)
print img
#show the image
cv2.imshow('image',img)
#hold the image for 5sec 
k = cv2.waitKey(0) & 0xFF
if k ==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
# to write copy the image
    cv2.imwrite('messi5_copy.png',img)
    cv2.destroyAllWindows()
