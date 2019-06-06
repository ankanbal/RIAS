import os
import pyttsx3 as pt

os.system("tput setaf 1")
print("\t\t\tWelcome to the automation testing section\n")
os.system("tput setaf 0")
x=pt.init()
x.say("Press 1: to take a picture")
x.runAndWait()
x.say("Press 2: to start a video")
x.runAndWait()
x.say("Press 3: to make a TikTok video")
x.runAndWait()
x.say("Press 4: to make a rain check today")
x.runAndWait()
x.say("Press 5: to use the kid's playzone")
x.runAndWait()
x.say("Press anything else to exit")
x.runAndWait()
dic={}
loc_rem=input("Where do you want to run the commands local/remote?")
if loc_rem=="local":
	k=True
	while k==True:
		x.say("Please enter your choice")
		x.runAndWait()
		print("\n")
		ch=input()
		if ch=="1":
			os.system("python3 /root/new/video.py")
			k=True
		elif ch=="2":
			os.system("python36 /root/new/phtot.py")
			k=True
		elif ch=="3":
			os.system("python36 /root/new/pythocode.py")
			k=True
		elif ch=="4":
			os.system("python36 /root/new/rain.py")
			k=True
		elif ch=="5":
			os.system("python36 /root/new/playzone.py")
			k=True
		else:
			k=False
else:
	ip_add=input("Enter the root user ip address")
	ip_pass=""
	
	if len(dic)==0:
		ip_pass=input("Enter the root password")
		kk=input("Do you want to save the ip and password? yes/no")
		if kk=="yes":
			dic[ip_add]=ip_pass
	else:
		for yy in dic.keys():
			if yy==ip_add:
				ip_pass=dic[ip_add]
				break
	
	if len(ip_pass)==0
		ip_pass=input("Enter the root password")
		kk=input("Do you want to save the ip and password? yes/no")
		if kk=="yes":
			dic[ip_add]=ip_pass
	
	k=True
	os.system("sshpass -p "+dic[ip_add]+" ssh -X root@"+ip_add)
	while k==True:
		x.say("Please enter your choice")
		x.runAndWait()
		print("\n")
		ch=input()
		if ch=="1":
			os.system("python36 /root/new/video.py ")
			k=True
		elif ch=="2":
			os.system("sshpass -p "+dic[ip_add]+" ssh -X python36 /root/new/phtot.py root@"+ip_add)
			k=True
		elif ch=="3":
			os.system("sshpass -p "+dic[ip_add]+" ssh -X python36 /root/new/pythocode.py root@"+ip_add)
			k=True
		elif ch=="4":
			os.system("sshpass -p "+dic[ip_add]+" ssh -X python36 /root/new/rain.py root@"+ip_add)
			k=True
		elif ch=="5":
			os.system("sshpass -p "+dic[ip_add]+" ssh -X python36 /root/new/playzone.py root@"+ip_add)
			k=True
		else:
			k=False
	

x.say("Thank you for using our voice commands service")
x.runAndWait()


