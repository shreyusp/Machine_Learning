

from sklearn.datasets import load_iris
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

userInput=input("Sepal Length, Sepal Width,Petal Length, Petal Width:")
userInput=userInput.split(',')
u=[]
for item in userInput:
    try:
        u.append(float(item))
    except:
        u.append(item.lower())
u=np.array(u).reshape(1,-1)

ypred=classifier.predict(u)
print(target_names[ypred])