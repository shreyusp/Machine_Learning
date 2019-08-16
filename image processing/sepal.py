from sklearn.datasets import load_iris
iris=load_iris()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(x_train,y_train)
 
from sklearn.externals import joblib
joblib.dump(classifier,'irisPred.sav')

#doesnt wok