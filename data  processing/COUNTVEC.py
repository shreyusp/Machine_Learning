import pandas as pd
import numpy as np
data=pd.read_table('data.tsv',header=None,names=['label','message'])
data['label_num']=data.label.map({'ham':0,'spam':1})
x=data.iloc[:,1]
y=data.iloc[:,2]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)

from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer()
x_train=vect.fit_transform(x_train)
x_test=vect.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train,y_train)
score=clf.score(x_test,y_test)
print(score)

from sklearn.svm import LinearSVC
sclf=LinearSVC()
sclf.fit(x_train,y_train)
score=sclf.score(x_test,y_test)
print(score)

from sklearn.naive_bayes import MultinomialNB
nclf=MultinomialNB()
nclf.fit(x_train,y_train)
score=nclf.score(x_test,y_test)
print(score)
