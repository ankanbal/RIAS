import pyttsx3 as pt
import pandas as pd
from sklearn.linear_model import LinearRegression


x=pd.read_csv("/root/Desktop/corporate.csv")
years=x.iloc[:,6:7]
#hr=x.iloc[:,6]
salary=x.iloc[:,1]
'''import numpy as np
print(np.shape(hrs))
print(np.shape(marks))'''
mind=LinearRegression()
mind.fit(years,salary)
ch=input("Enter the years to check the  deserving salary")
xx=mind.predict([[ch]])

speak=pt.init()
str1="The person has "+str(ch)+" years experience of work so his deserving salary is "+xx[0]+"."
speak.say(str1)
speak.runAndWait()
if xx[0]>=100000:
	str2="This person cannot be hired, unaffordable by the company."
	speak.say(str2)
	speak.runAndWait()
else:
	str3="This man can be afforded by the company."
	speak.say(str3)
	speak.runAndWait()
