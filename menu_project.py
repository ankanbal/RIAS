#!/usr/bin/env python
# coding: utf-8

# In[14]:


#library modules

import pyttsx3 as py
import speech_recognition as sr
import subprocess as sp
import os
import socket
import random as rn
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from datetime import datetime
from colorama import Fore


# In[15]:


#initializations
sock =  socket.socket()
sock.connect(("192.168.43.217" , 3333))
mic = sr.Microphone()
rec = sr.Recognizer()
x=py.init()
voices=x.getProperty('voices')
#l=py.voice.Voice(voices[1].id)
x.setProperty('voice', voices[1].id)
rate = x.getProperty('rate')
x.setProperty('rate', 175)
BUFFER=1024
lz= [0]*16
#l.age
#print(rate)
#print(volume)
#print(voices)


# In[16]:


print(cv2.__version__)
# Get the training data we previously made
data_path = 'G:\\test\\'
# a=listdir('d:/faces')
# print(a)
# """
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and laels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
# 
# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
model=cv2.face_LBPHFaceRecognizer.create()
# Initialize facial recognizer
# model = cv2.face_LBPHFaceRecognizer.create()
# model=cv2.f
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# Let's train our model 
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")


# In[17]:


#functions definitions

def recog():
    face_classifier = cv2.CascadeClassifier('C:\\Users\\Ankan Bal\\AppData\\Roaming\\SPB_Data\\new\\haarcascade_frontalface_default.xml')
    def face_detector(img, size=0.5):    
    # Convert image to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if faces is ():
            return img, []
    
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200, 200))
        return img, roi


# Open Webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        image, face = face_detector(frame)
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
            results = model.predict(face)
            print(results)
            if results[1] < 500:
                confidence = int( 100 * (1 - (results[1])/400) )
                display_string = str(confidence) + '% Confident it is User'

            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
            if confidence > 75:
                cv2.putText(image, "Hey Boss", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face Recognition', image )
                cap.release()
                cv2.destroyAllWindows()
                main()
                break
            else:
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.imshow('Face Recognition', image )

        except:
            #cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            #cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            #cv2.imshow('Face Recognition', image )
            pass
        
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
        
    #cap.release()
    #cv2.destroyAllWindows()
def sarcasm():
    sar1="How many times has it been boss? "
    sar2="Come on, its been three times already. "
    sar3="Boss, are you alright, asking me three times for a single command. "
    sar4="Don't you trust me boss? "
    ls=[sar1,sar2,sar3,sar4]
    i=rn.randint(0,3)
    x.say(ls[i])
    x.runAndWait()

def jokes():
    jk1="Please don't joke with me boss. "
    jk2="Yes,     funny. Now please onto business again. "
    jk3="Don't get your hopes high boss. I am just a program. "
    jk4="What?    Were you really expecting me to do that? "
    ls=[jk1,jk2,jk3,jk4]
    i=rn.randint(0,3)
    x.say(ls[i])
    x.runAndWait()
    
def okSay():
    st1="OK Boss."
    st2="Understood."
    st3="Got it."
    st4="Alright Boss."
    st5="Consider it done."
    st6="With Pleasure."
    st7="Very well boss"
    ls=[st1,st2,st3,st4,st5,st6,st7]
    i=rn.randint(0,6)
    x.say(ls[i])
    x.runAndWait()
        
def introSay():
    tim=datetime.now().time()
    tim=str(tim)
    k=tim.split(":")
    t=int(k[0])
    if t>=4 and t<12:
        x.say("Good Morning Boss")
        x.runAndWait()
    elif t>=12 and t<17:
        x.say("Good Afternoon Boss")
        x.runAndWait()
    elif t>=17 and t<20:
        x.say("Good Evening Boss")
        x.runAndWait()

def canDo():
    x.say("Well I can launch a docker, an E C 2 instance, or maybe I can configure some services for you. Or maybe run some Machine Learning models. Below I have mentioned the things that I can do.")
    x.runAndWait()
    print('''
    1: Run a docker using playbook
    2: Configure firewall using ansible playbook
    3: Start firefox as software as a service
    4: Start EC2 instance using ansible playbook
    5: Send a mail using ansible playbook
    6: Configure yum using playbook
    7: Configure web server using playbook
    8: Configure datanode in hdfs cluster using playbook
    9: Install java and hadoop and setting path variables
    10: Apply Machine Learning using two variable Linear Regression
    11: Apply Machine Learning using multi variable Linear Regression
    12: Apply Deep Learning using two variable Linear Regression
    13: Apply Deep Learning using multi variable Linear Regression
    14: Apply Machine Learning using multi variable Logistic Regression''')

def dateRun():
    print("Date Run...........")
    st0="date"
    print(st0)
    lz[0]+=1
    if lz[0]>=3:
        sarcasm()
    #sock.send(st0.encode())
    #print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
        
def dockerRun():
    print("Docker Run...........")
    st1="ansible-playbook /root/ansible_playbooks/dockerRun.yml"
    print(st1)
    sock.send(st1.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook dockerRun.yaml")
    
def fireWalle():
    print("Enabling firewall..............")
    st2="ansible-playbook /root/ansible_playbooks/fireWalle.yml"
    print(st2)
    sock.send(st2.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook fireWalle.yaml")
    
def fireWalld():
    print("Disabling firewall............")
    st3="ansible-playbook /root/ansible_playbooks/fireWalld.yml"
    print(st3)
    sock.send(st3.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook fireWalld.yaml")
    
def firefoxSAAS():
    print("firefox SAAS enabling...........")
    st4="ansible-playbook /root/ansible_playbooks/firefoxSAAS.yml"
    print(st4)
    sock.send(st4.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook firefoxSAAS.yaml")
    
def instanceEC2():
    print("EC2 instance")
    st5="ansible-playbook /root/ansible_playbooks/instanceEC2.yml"
    print(st5)
    sock.send(st5.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook instanceEC2.yaml")
    
def sendMail():
    print("Sending mail.......")
    st6="ansible-playbook --ask-vault-pass /root/ansible_playbooks/sendMail.yml"
    print(st6)
    sock.send(st6.encode())
    #passw=input()
    #sock.send("")
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook sendMail.yaml")

def confYum():
    print("Yum configuring")
    st7="ansible-playbook /root/ansible_playbooks/confYum.yml"
    print(st7)
    sock.send(st7.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook confYum.yaml")
    
def confWebe():
    print("Enabling web server.......")
    st8="ansible-playbook /root/ansible_playbooks/confWebe.yml"
    print(st8)
    sock.send(st8.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    #os.system("ansible-playbook confWebe.yaml")
    
def confWebd():
    print("Disabling web server.......")
    st9="ansible-playbook /root/ansible_playbooks/confWebd.yml"
    print(st9)
    sock.send(st9.encode())
    print(sock.recv(BUFFER).decode())
    x.say("What else boss?")
    x.runAndWait()
    print("Disable web server")
    #os.system("ansible-playbook confWebd.yaml")
    
'''def hdfsNode():
    os.system("ansible-playbook hdfsNode.yaml")

def javaHadoop():
    os.system("ansible-playbook javaHadoop.yaml")'''

'''def linearML():
    print("LinearML")
    #os.system("ansible-playbook linearML.yaml")

def mlinearML():
    print("mLinearML")
    #os.system("ansible-playbook mlinearML.yaml")
    
def linearDL():
    print("LinearDL")
    #os.system("ansible-playbook linearDL.yaml")
    
def mlinearDL():
    print("mLineaarDL")
    #os.system("ansible-playbook mlinearDL.yaml")
    
def mLogistic():
    print("mLogistic")
    #os.system("ansible-playbook mLogistic.yaml")'''


# In[18]:


#main code
def main():
    print(Fore.RED +"\t\t\tWelcome to the automation testing section. RIAS loves to help people\n")
    print('''
                                :-+*+===+***+==-::::                           
                              ::-*****************+-:                          
                              ::********************-:                         
                        ::::::-#********************+::                        
                     :::=+****%@@%#******************-::                       
                     ::*******#%@@@@%%##************##-::::                    
                     ::=********##%@@@@@@@@%%%%%%%%@@@#**=:::                  
                      :::+**********##%%%@@@@@@@@@@@%#*****=::                 
                        :::-+*****************##************:                  
                           ::::-=+*************************-::                 
                               :::::--=++**************+=-:::                  
                                       :::::::::::::::::                       
                                       :::                                     
    +++++++++=-:                   ::+*#+:  :=+++:   ::+++-:           ::=++:  
    %@@@####@@@%-::::---:::   :::---:%@@*:  :*@@@:    -@@@=::::---::::::*@@@:::
    %@@#::::=@@@+:*%@@@@@%+:::+%@@@@@@@@*:  :*@@@=====+@@@=:#@@@@@@@#:*@@@@@@@%
    %@@@@@@@@@%+:@@@#+++%@@*:%@@*-:::%@@*:  :*@@@@@@@@@@@@=::+====%@@*::+@@%:::
    %@@#--=@@@*::@@@%******+:@@@+::::%@@*:  :*@@@:::::-@@@==@@%***@@@* :+@@@:::
    %@@*: ::*@@%=-+#%@%%@%=:::+#%@%%%%@@*:  :+@@%:   :-@@@=-#%%###%@@* :-#%@@%* \n''')
    introSay()
    x.say("HI I am Rias, a Responsive Intelligent Automation System, at your service. How may I help you?")
    x.runAndWait()
    '''x.say("Say 1: to run a docker using playbook")
    x.runAndWait()
    x.say("Say 2: to configure firewall using ansible playbook")
    x.runAndWait()
    x.say("Say 3: to use firefox as software as a service")
    x.runAndWait()
    x.say("Say 4: to start EC2 instance using ansible playbook")
    x.runAndWait()
    x.say("Say 5: to send a mail using ansible playbook")
    x.runAndWait()
    x.say("Say 6: to configure yum using playbook")
    x.runAndWait()
    x.say("Say 7: to configure web server using playbook")
    x.runAndWait()
    x.say("Say 8: to configure datanode in hdfs cluster using playbook")
    x.runAndWait()
    x.say("Say 9: to install java and hadoop and setting path variables")
    x.runAndWait()
    x.say("Say 10: to create a socket and client connection")
    x.runAndWait()
    x.say("Say 11: to apply Machine Learning using two variable Linear Regression")
    x.runAndWait()
    x.say("Say 12: to apply Machine Learning using multi variable Linear Regression")
    x.runAndWait()
    x.say("Say 13: to apply Deep Learning using two variable Linear Regression")
    x.runAndWait()
    x.say("Say 14: to apply Deep Learning using multi variable Linear Regression")
    x.runAndWait()
    x.say("Say 15: to apply Machine Learning using multi variable Logistic Regression")
    x.runAndWait()
    x.say("Say I am done to exit")
    x.runAndWait()'''
    while True:
        with mic as source:
            print("say : ")
            audio = rec.listen(source)
            data = rec.recognize_google(audio)
            print(data)

        #docker
        if "what" in data and "can" in data and "do" in data:
            canDo()
            
        elif "date" in data:
            okSay()
            dateRun()
            
        elif "docker" in data and not "don't" in data:
            okSay()
            dockerRun()
        elif "docker" in data and "don't" in data:
            x.say("Well, not docker then. What else can I do for you?")
            x.runAndWait()

        #firewall

        elif "firewall" in data and "enable" in data and not "don't" in data:
            okSay()
            fireWalle()
        elif "firewall" in data and "disable" in data and not "don't" in data:
            okSay()
            fireWalld()
        elif "firewall" in data and "enable" in data and "don't" in data:
            x.say("Well, should I disable it then?")
            x.runAndWait()
            with mic as source:
                print("say : ")
                audio = rec.listen(source)
                data = rec.recognize_google(audio)
                print(data)
            if "yes" in data or "alright" in data:
                okSay()
                fireWalld()
            elif "no" in data:
                x.say("Well, not disabling firewall then. What else can I do for you?")
                x.runAndWait()
        elif "firewall" in data and "disable" in data and "don't" in data:
            x.say("Well, should I enable it then?")
            x.runAndWait()
            with mic as source:
                print("say : ")
                audio = rec.listen(source)
                data = rec.recognize_google(audio)
                print(data)
            if "yes" in data or "alright" in data:
                okSay()
                fireWalle()
            elif "no" in data:
                x.say("Well, not enabling firewall then. What else can I do for you?")
                x.runAndWait()

        #firefox

        elif "firefox" in data and "software as a service" in data and not "don't" in data:
            okSay()
            firefoxSAAS()
        elif "firefox" in data and "software as a service" in data and not "don't" in data:
            x.say("Well, not firefox then. What else can I do for you?")
            x.runAndWait()

        #EC2 instance

        elif "EC 2 instance" in data or "EC to instance" in data and "run" in data and not "don't" in data:
            okSay()
            instanceEC2()
        elif "EC 2 instance" in data or "EC to instance" in data and "run" in data and "don't" in data:
            x.say("Well, not EC2 then. What else can I do for you?")
            x.runAndWait()

        #mail

        elif "mail" in data and "send" in data and not "don't" in data:
            okSay()
            sendMail()
        elif "mail" in data and "send" in data and "don't" in data:
            x.say("Well, no mails then. What else can I do for you?")
            x.runAndWait()

        #yum

        elif "Yum" in data and "configure" in data and not "don't" in data:
            okSay()
            confYum()
        elif "Yum" in data and "configure" in data and "don't" in data:
            x.say("Well, not yum configuration then. What else can I do for you?")
            x.runAndWait()

        #web server

        elif "web server" in data and "enable" in data and not "don't" in data:
            okSay()
            confWebe()
        elif "web server" in data and "disable" in data and not "don't" in data:
            okSay()
            confWebd()
        elif "web server" in data and "enable" in data and "don't" in data:
            x.say("Well, should I disable it then?")
            x.runAndWait()
            with mic as source:
                print("say : ")
                audio = rec.listen(source)
                data = rec.recognize_google(audio)
                print(data)
            if "yes" in data or "alright" in data:
                okSay()
                confWebd()
            elif "no" in data:
                x.say("Well, not disabling web server then. What else can I do for you?")
                x.runAndWait()
        elif "web server" in data and "disable" in data and "don't" in data:
            x.say("Well, should I enable it then?")
            x.runAndWait()
            with mic as source:
                print("say : ")
                audio = rec.listen(source)
                data = rec.recognize_google(audio)
                print(data)
            if "yes" in data or "alright" in data:
                okSay()
                confWebe()
            elif "no" in data:
                x.say("Well, not enabling web server then. What else can I do for you?")
                x.runAndWait()

        #Linear Regression ML

        '''elif "linear regression" in data and "run" in data and not "deep learning" in data and not "don't" in data:
            okSay()
            linearML()
        elif "linear Regression" in data and "run" in data and not "deep learning" in data and "don't" in data:
            x.say("Well, no Linear Regression then. What else can I do for you?")
            x.runAndWait()

        #multi Linear Regression ML

        elif "multi variable linear regression" in data and "run" in data and not "deep learning" in data and not "don't" in data:
            okSay()
            mlinearML()
        elif "multi variable linear regression" in data and "run" in data and not "deep learning" in data and "don't" in data:
            x.say("Well, no Multi Linear Regression then. What else can I do for you?")
            x.runAndWait()

        #Linear Regression DL

        elif "linear regression" in data and "run" in data and "deep learning" in data and not "don't" in data:
            okSay()
            linearDL()
        elif "linear regression" in data and "run" in data and "deep learning" in data and "don't" in data:
            x.say("Well, no Linear Deep Learning then. What else can I do for you?")
            x.runAndWait()

        #multi Linear Regression DL

        elif "multi variable linear regression" in data and "run" in data and "deep learning" in data and not "don't" in data:
            okSay()
            mlinearDL()
        elif "multi variable linear regression" in data and "run" in data and "deep learning" in data and "don't" in data:
            x.say("Well, no Multi Linear Deep Learning then. What else can I do for you?")
            x.runAndWait()

        #Logistic Regression

        elif "logistic regression" in data and "run" in data and not "don't" in data:
            okSay()
            mLogistic()
        elif "logistic regression" in data and "run" in data and "don't" in data:
            x.say("Well, no Logistic Regression I guess. What else can I do for you?")
            x.runAndWait()'''

        elif "i am done" in data or "I am done" in data:
            tim=datetime.now().time()
            tim=str(tim)
            k=tim.split(":")
            t=int(k[0])
            if t>=20 and t<=23:
                x.say("Good night boss. Happy to help.")
                x.runAndWait()
                print("Good night boss. Happy to help.")
            else:
                x.say("Have a good day boss....")
                x.runAndWait()
                print("Have a good day boss....")
            break

        elif "sing" in data or "dance" in data or "play" in data:
            jokes()
        
        else:
            x.say("I am not sure if I got that correct. Or maybe that feature is not available. Can I help you with something else? ")
            x.runAndWait()
            print("we dont support this")


# In[19]:


recog()


# In[ ]:




