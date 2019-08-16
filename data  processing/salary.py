import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
data2=pd.read_csv('Salary_Data.csv')
c=data2["YearsExperience"].values
d=data2.iloc[:,1].values



x=data2.iloc[:,0:1].values
y=data2.iloc[:,1].values
plt.scatter(x,y,color='red')
#---------------------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x_train,y_train)
m=regressor.coef_
c=regressor.intercept_

y75=(m*7.5)+c
yP75=regressor.predict([[7.5]])
y_pred=regressor.predict(x_test)

plt.scatter(x_train,y_train,color='red') 
plt.scatter(x_test,regressor.predict(x_test),color='green')
plt.scatter(x_test,y_test,color='blue')

plt.plot(x_train,regressor.predict(x_train),color='blue')

#--------------------------------------------------------------------------------------------
a=input("Enter stuff")
a=a.split(',')
result=[]
n=0
for x in a:
    result.append(x)
    n=n+1
result=np.array(result)
result=result.reshape((len(result),1))
regressor.predict(result)
sum1=0
for i in range(n):
   rm=(y_pred-result[i])**2
   sum1=sum1+rm
res=math.sqrt((1/n)*sum1)
print(res)
   


    


