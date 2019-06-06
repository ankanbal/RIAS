import cv2


x=cv2.VideoCapture(0)
ret , photo = x.read()
x.release()
cv2.imwrite("/root/photo.png" ,photo)
#cv2.waitKey(5000)
#cv2.destroyAllWindows()


