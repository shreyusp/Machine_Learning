import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#a=["delhi","Bangalore","Chennai","Mumbai"]

data3=pd.read_csv('Position_Salaries.csv')
x=data3.iloc[:,1:2].values
y=data3.iloc[:,2].values
plt.scatter(x,y)
from sklearn.linear_model import LinearRegression
lregressor=LinearRegression()
lregressor.fit(x,y)
lregressor.fit(x,y)
plt.plot(x,lregressor.predict(x),'red')

from sklearn.preprocessing import PolynomialFeatures
polyfeatures=PolynomialFeatures(degree=2)
xPoly=polyfeatures.fit_transform(x)

polyRegressor=LinearRegression()
polyRegressor.fit(xPoly,y)
plt.plot(x,polyRegressor.predict(xPoly),'green')
print(polyRegressor.score(xPoly,y))

score=0
d=2
ypred=[]
while score<=.9997:
    polyfeatures=PolynomialFeatures(degree=d)
    xPoly=polyfeatures.fit_transform(x)
    polyRegressor=LinearRegression()
    polyRegressor.fit(xPoly,y)
    ypred.append(polyRegressor.predict(xPoly))
    score=polyRegressor.score(xPoly,y)
    d+=1
print(d)
position=1
for prediction in ypred:
    plt.subplot(2,2,position)
    plt.scatter(x,y,color='blue')
    plt.plot(x,prediction,'green')
    position+=1

    

