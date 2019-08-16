import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data2=pd.read_csv('insurance.csv')
x=data2.iloc[:,:6].values
y=data2.iloc[:,6].values

from sklearn.preprocessing import LabelEncoder
Encoder1=LabelEncoder()
x[:,1]=Encoder1.fit_transform(x[:,1])
Encoder2=LabelEncoder()
x[:,4]=Encoder2.fit_transform(x[:,4])
Encoder3=LabelEncoder()
x[:,5]=Encoder3.fit_transform(x[:,5])


from sklearn.preprocessing import OneHotEncoder
ohEncoder1=OneHotEncoder(categorical_features=[5])
x=ohEncoder1.fit_transform(x).toarray()
x=x[:,1:]
 

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x_train,y_train)            #finding B0 and B1 ie m and c (eqn of a line)
y_pred=regressor.predict(x_test)
userInput=input("Enter Age,Sex,Bmi,Children,Smoker,region:")
userInput=userInput.split(',')
u=[]
for item in userInput:
    try:
        u.append(float(item))
    except:
        u.append(item.lower())
u=np.array(u).reshape(1,-1)


u[:,1]=Encoder1.fit_transform(u[:,1])
u[:,4]=Encoder2.fit_transform(u[:,4])
u[:,5]=Encoder3.fit_transform(u[:,5])

u=ohEncoder1.transform(u).toarray()

u=u[:,1:]
print(regressor.predict(u))


#Encoder1.transform('male')
#Encoder1.transform('female')

