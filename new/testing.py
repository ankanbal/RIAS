import cv2
import os

os.system("python36 /root/Desktop/testing2.py")
x=cv2.VideoCapture(0)


while True:
	ret,photo=x.read()
	cv2.imshow("My video",photo)
	if cv2.waitKey(1)==13:
		break

cv2.destroyAllWindows()





