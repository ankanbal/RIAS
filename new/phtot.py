#!/usr/bin/env python
# coding: utf-8

# In[24]:


import cv2 # importing cv2 module


# In[30]:


x = cv2.VideoCapture(0) # accessing webcam


# In[11]:


# taking a photo


# In[16]:


# live video
while True:
    ret , video = x.read()
    cv2.imshow("live footage" , video)
    if cv2.waitKey(1) == 13:
        break
        
x.release()
cv2.destroyAllWindows()


# In[31]:


# live cropped video
while True:
    ret , video = x.read()
    frame = video[120:400 , 200:480] # cropping frame
    cv2.imshow("frame" , frame)
    if cv2.waitKey(1) == 13:
        break
        
x.release()
cv2.destroyAllWindows()
    


# In[ ]:




