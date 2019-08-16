import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
data=pd.read_csv('Social_Network_Ads.csv')
x=data.iloc[:,1:4].values
y=data.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder
lencoder=LabelEncoder()
x[:,0]=lencoder.fit_transform(x[:,0])

from sklearn.preprocessing import StandardScaler
sscaler=StandardScaler()
x=sscaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train,y_train)
ypred=clf.predict(x_test)


from sklearn.metrics import confusion_matrix
'''
The no of correct predictions in cmis f00 and f11
The difference btwregrssion and classification is that in regression we can 
determine the distance btw points
Classification ifs used to classify the points into sets'''
cm=confusion_matrix(y_test,ypred)
print(cm)

result=['Female',27,57000]
result=np.array(result)
result=result.reshape((1,-1))

result[:,0]=lencoder.fit_transform(result[:,0])
sscalerv=sscaler.transform(result)
print(clf.predict(sscalerv))

  
def distance(x1,x2):
    return np.sqrt(((x1-x2)**2).sum())

def knn(testinput,x,y,k):
    numrows=x.shape[0]
    dist=[]
    for item in range(numrows):
        dist.append(distance(testinput,x[item]))
    dist=np.array(dist)
    index=np.argsort(dist)
    sortedLabels=y[index][:k]
    count=np.unique(sortedLabels,return_counts=True)
    return count[0][np.argmax(count[-1])]    
 
knn(sscalerv,x_train,y_train,3)
yprednew.append(knn(x_test[i],x_train,y_train,3))

import cv2