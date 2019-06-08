#!/usr/bin/env python
# coding: utf-8

# In[42]:


#library modules

import pyttsx3 as py
import speech_recognition as sr
import subprocess as sp
import os
import random as rn
from datetime import datetime


# In[43]:


#initializations

mic = sr.Microphone()
rec = sr.Recognizer()
x=py.init()
voices=x.getProperty('voices')
l=py.voice.Voice(voices[1].id)
x.setProperty('voice', voices[1].id)
rate = x.getProperty('rate')
x.setProperty('rate', 150)
l.age
#print(rate)
#print(volume)
#print(voices)


# In[44]:


#functions definitions

def okSay():
    st1="OK Boss."
    st2="Understood."
    st3="Got it."
    st4="Alright."
    st5="Consider it done."
    ls=[st1,st2,st3,st4,st5]
    i=rn.randint(0,5)
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
    
def dockerRun():
    print("Docker run")
    #os.system("ansible-playbook dockerRun.yaml")
    
def fireWalle():
    print("Enable firewall")
    #os.system("ansible-playbook fireWalle.yaml")
    
def fireWalld():
    print("Disable firewall")
    #os.system("ansible-playbook fireWalld.yaml")
    
def firefoxSAAS():
    print("firefox SAAS")
    #os.system("ansible-playbook firefoxSAAS.yaml")
    
def instanceEC2():
    print("EC2 instance")
    #os.system("ansible-playbook instanceEC2.yaml")
    
def sendMail():
    print("Mail sent")
    #os.system("ansible-playbook sendMail.yaml")

def confYum():
    print("Yum configured")
    #os.system("ansible-playbook confYum.yaml")
    
def confWebe():
    print("Enable web server")
    #os.system("ansible-playbook confWebe.yaml")
    
def confWebd():
    print("Disable web server")
    #os.system("ansible-playbook confWebd.yaml")
    
'''def hdfsNode():
    os.system("ansible-playbook hdfsNode.yaml")

def javaHadoop():
    os.system("ansible-playbook javaHadoop.yaml")'''
    
def clientSocket():
    x.say("Are you the Client or the Server?")
    x.runAndWait()
    with mic as source:
        print("say : ")
        audio = rec.listen(source)
        data = rec.recognize_google(audio)
        print(data)
    if data=="server":
        print("server")
        #os.system("python3 server.py")
    elif data=="client":
        print("client")
        #os.system("python3 client.py")

def linearML():
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
    #os.system("ansible-playbook mLogistic.yaml")


# In[ ]:


#main code

print("\t\t\tWelcome to the automation testing section\n")
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
    
    if "docker" in data and not "don't" in data:
        okSay()
        dockerRun()
    elif "docker" in data and "don't" in data:
        x.say("Well, not docker then. What else can I do for you?")
        x.runAndWait()
    
    #firewall
    
    if "firewall" in data and "enable" in data and not "don't" in data:
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
    
    if "firefox" in data and "software as a service" in data and not "don't" in data:
        okSay()
        firefoxSAAS()
    elif "firefox" in data and "software as a service" in data and not "don't" in data:
        x.say("Well, not firefox then. What else can I do for you?")
        x.runAndWait()
    
    #EC2 instance
    
    if "EC2 instance" in data and "run" in data and not "don't" in data:
        okSay()
        instanceEC2()
    elif "EC2 instance" in data and "run" in data and "don't" in data:
        x.say("Well, not EC2 then. What else can I do for you?")
        x.runAndWait()

    #mail
    
    if "mail" in data and "send" in data and not "don't" in data:
        okSay()
        sendMail()
    elif "mail" in data and "send" in data and "don't" in data:
        x.say("Well, no mails then. What else can I do for you?")
        x.runAndWait()

    #yum
    
    if "yum" in data and "configure" in data and not "don't" in data:
        okSay()
        confYum()
    elif "yum" in data and "configure" in data and "don't" in data:
        x.say("Well, not yum configuration then. What else can I do for you?")
        x.runAndWait()
    
    #web server
    
    if "web server" in data and "enable" in data and not "don't" in data:
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


    #elif data=="eight":
    #    hdfsNode()
    #elif data=="nine":
    #    javaHadoop()
    
    #client server
    if "client server" in data and not "don't" in data:
        okSay()
        clientSocket()
    elif "client server" in data and "don't" in data:
        x.say("Well, fine then. What else can I do for you?")
        x.runAndWait()
    
    #Linear Regression ML
    
    if "Linear Regression" in data and "run" in data and not "Deep Learning" in data and not "don't" in data:
        okSay()
        linearML()
    elif "Linear Regression" in data and "run" in data and not "Deep Learning" in data and "don't" in data:
        x.say("Well, no Linear Regression then. What else can I do for you?")
        x.runAndWait()

    #multi Linear Regression ML
    
    if "multi variable Linear Regression" in data and "run" in data and not "Deep Learning" in data and not "don't" in data:
        okSay()
        mlinearML()
    elif "multi variable Linear Regression" in data and "run" in data and not "Deep Learning" in data and "don't" in data:
        x.say("Well, no Multi Linear Regression then. What else can I do for you?")
        x.runAndWait()

    #Linear Regression DL
    
    if "Linear Regression" in data and "run" in data and "Deep Learning" in data and not "don't" in data:
        okSay()
        linearDL()
    elif "Linear Regression" in data and "run" in data and "Deep Learning" in data and "don't" in data:
        x.say("Well, no Linear Deep Learning then. What else can I do for you?")
        x.runAndWait()

    #multi Linear Regression DL
    
    if "multi variable Linear Regression" in data and "run" in data and "Deep Learning" in data and not "don't" in data:
        okSay()
        mlinearDL()
    elif "multi variable Linear Regression" in data and "run" in data and "Deep Learning" in data and "don't" in data:
        x.say("Well, no Multi Linear Deep Learning then. What else can I do for you?")
        x.runAndWait()

    #Logistic Regression
    
    if "Logistic Regression" in data and "run" in data and not "don't" in data:
        okSay()
        mLogistic()
    elif "Linear Regression" in data and "run" in data and "don't" in data:
        x.say("Well, no Logistic Regression I guess. What else can I do for you?")
        x.runAndWait()

    elif "i am done" in data or "I am done":
        x.say("Have a good day boss....")
        x.runAndWait()
        break
    else:
        x.say("I am not sure if I got that correct. Or maybe that feature is not available. Can I help you with something else? ")
        speaker.runAndWait()
        print("we dont support this")


# In[ ]:




