#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


cap=cv2.VideoCapture(0)


# In[3]:


while True:
        ret,frame=cap.read()
        #ret,frame1=cap.read()
        n=frame[50:250,209:409]
        frame[0:200,439:639]=n
        d=frame[100:300,200:400]
        frame[0:200,0:200]=d
        a=frame[200:400,100:300]
        frame[279:479,0:200]=a
        cv2.imshow("mihir2" , frame)
        if cv2.waitKey(1)==13:
            break
cap.release()
cv2.destroyAllWindows()

