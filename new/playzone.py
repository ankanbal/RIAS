
# coding: utf-8

# In[12]:


import pyttsx3 as pt


# In[15]:


speaker = pt.init()
speaker.say("Enter your name")
speaker.runAndWait()
name = input()
speaker.say(f"Hello {name}, how are you")
speaker.runAndWait()


# In[16]:


speaker.say("press 1 to play baby poems")
speaker.say("press 2 to play  A B C")
speaker.say("press 3 to play 1 2 3")
speaker.say("press 4 to close me")
speaker.runAndWait()


# In[ ]:


x = int(input())
while True:
    if x == 1:
        speaker.say("Johny Johny Yes Papa Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah, ah! Johny, Johny Yes, Papa? Eating sugar? No, papa! Telling lies? No, papa! Open your mouth Ah, ah,… ")
        speaker.say("Twinkle, twinkle, little star, How we wonder what you are. Up above the world so high, Like a diamond in the sky. When the glorious sun has set, And the grass with dew is wet, Then you show your little light, Twinkle, twinkle, all the night. When the golden sun doth rise, Fills with shining light the skies, Then you fade away from sight, Shine no more 'till comes the night.")
        speaker.runAndWait()
    elif x == 2:
        speaker.say("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
        speaker.runAndWait()
    elif x == 3:
        speaker.say("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50")
        speaker.runAndWait()
    elif x == 4:
        speaker.say("Bye Bye Friend")
        speaker.runAndWait()
        break
    else:
        speaker.say("Friend you pressed wrong key, press 1 to play baby poems, press 2 to play  A B C, press 3 to play 1 2 3")
        speaker.runAndWait()
    speaker.say("press 1 to play baby poems")
    speaker.say("press 2 to play  A B C")
    speaker.say("press 3 to play 1 2 3")
    speaker.say("press 4 to close me")
    speaker.runAndWait()
    x = int(input())

