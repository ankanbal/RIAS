import pyttsx3 as pt
import pandas as pd
from sklearn.linear_model import LinearRegression


x=pd.read_csv("/root/new/rain.csv")
hrs=x.iloc[:,6:7]
hr=x.iloc[:,6]
marks=x.iloc[:,1]
'''import numpy as np
print(np.shape(hrs))
print(np.shape(marks))'''
mind=LinearRegression()
mind.fit(hrs,marks)

ch=input("Enter today's date")
xx=mind.predict([[ch]])

speak=pt.init()
str1="There is a "+str(xx[0])+" percent probability that it will rain today."
speak.say(str1)
speak.runAndWait()
if xx[0]>=65:
	str2="I think you would better take an umbrella today with you."
	speak.say(str2)
	speak.runAndWait()
else:
	str3="Its OK if u don't want to take an umbrella today."
	speak.say(str3)
	speak.runAndWait()
