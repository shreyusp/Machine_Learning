import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_digits
digits=load_digits()

images=digits.images
image=images[100]
plt.imshow(image)


for i in range(1,11):
    plt.subplot(3,2,i)
    plt.imshow(images[i],cmap='gray')
    plt.title(digits.target[i])


x=digits.data
y=digits.target

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



'''x=images.iloc[:,:6].values
y=images.iloc[:,6].values'''


