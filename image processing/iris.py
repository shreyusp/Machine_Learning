import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datsets import load_iris

iris=load_iris()
x=iris["data"]
y=iris.target
target_names=iris.target_names

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)
ypred=classifier.predict(x_test)
score=classifier.score(x_test,y_test)
print(score)

from sklearn.tree export graphviz
export_graphviz(model, out_file='tree.dot',feauture_names=iris.feauture_names,class_names=iris.target_names,
                rounded=True,filled=True,precision=2)


fromsklearn.tree import DecisionTreeClassifier