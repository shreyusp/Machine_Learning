import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data2=pd.read_csv('Churn_Modelling.csv')
x=data2.iloc[:,3:13].values
y=data2.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
genderen=LabelEncoder()
geographyen=LabelEncoder()

x[:,1]=genderen.fit_transform(x[:,1])
x[:,2]=geographyen.fit_transform(x[:,2])

from sklearn.preprocessing import OneHotEncoder
ohEncoder=OneHotEncoder(categorical_features=[3])

x=ohEncoder.fit_transform(x).toarray()
x=x[:,1:]

from sklearn.preprocessing import StandardScaler
sscaler=StandardScaler()
x=sscaler.fit_transform(x)

from keras.models import Sequential 
from keras.layers import Dense

model=Sequential()
model.add(Dense(units=6,activation='relu', input_dim=11))
model.add(Dense(units=6,activation='relu'))

model.add(Dense(units=6,activation='relu'))

history.


