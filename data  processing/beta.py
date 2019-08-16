import numpy as np
import pandas as pd
data1=pd.read_csv('headbrain.csv')
x=data1["Head Size(cm^3)"].values
y=data1["Brain Weight(grams)"].values

xmean=np.mean(x)
ymean=np.mean(y)

val1=0
val2=0
for i in range(len(x)):
    xdif=x[i]-xmean
    ydif=y[i]-ymean
    val1=val1+xdif*ydif
for i in range(len(x)):
    xdif=x[i]-xmean
    val2=val2+xdif**2

b1=val1/val2
b0=ymean-b1*xmean

print("Beta1: ",b1)
print("Beta0: ",b0)

#----------------------------------------------------------------------------------------

x1=data1.iloc[:,2:3].values
 
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x1,y)
m=regressor.coef_
c=regressor.intercept_
print(m)
print(c)

    
 


