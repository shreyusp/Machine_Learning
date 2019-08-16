import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
data3=pd.read_csv('Social_Network_Ads.csv')
x=data3.iloc[:,1:4].values
y=data3.iloc[:,4].values
#plt.scatter(x,y)

'''Produces a graph with two separated classes
use sigmoid function ie 1/(1-e**(-y)))
y=B0+B1x
standard scaling=(x-xmean)/Standard deviation(x-xmean)'''

from sklearn.preprocessing import LabelEncoder
lEncoder=LabelEncoder()
#We perform onehotencoding if we have multiple categorical attributes
x[:,0]=lEncoder.fit_transform(x[:,0])
from sklearn.preprocessing import StandardScaler
sscaler=StandardScaler()
x=sscaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)
ypred=classifier.predict(x_test)


count=0
for i in range(len(ypred)):
    if ypred[i]==y_test[i]:
        count+=1
print(count)
from sklearn.metrics import confusion_matrix
'''
The no of correct predictions in cmis f00 and f11
The difference btwregrssion and classification is that in regression we can 
determine the distance btw points
Classification ifs used to classify the points into sets'''
cm=confusion_matrix(y_test,ypred)
print(cm)


score=classifier.score(x_test,y_test)

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,ypred)**(1/2)

