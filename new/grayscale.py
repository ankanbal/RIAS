import cv2
cap=cv2.VideoCapture(0)
while True:
	ret,photo=cap.read()
	photo=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
	cv2.imshow("hiii",photo)
	if cv2.waitKey(1)==13:
		break
cv2.destroyAllWindows()
