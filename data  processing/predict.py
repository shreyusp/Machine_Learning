import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('headbrain.csv')
x_train=np.array(data.iloc[:100,2])             #(rowi:rowj,colk)
y_train=np.array(data.iloc[:100,3])
x_test=np.array(data.iloc[100:,2])             #(rowi:rowj,colk)
y_test=np.array(data.iloc[100:,3])

#Training
xm,ym=x_train.mean(),y_train.mean()
b1_num,b1_denom=0,0
for i in range(len(x_train)):
    b1_num+=(x_train[i]-xm)*(y_train[i]-ym)
    b1_denom+=(x_train[i]-xm)**2
b1=b1_num/b1_denom
b0=ym-b1*xm

#test
y_pred=b1*x_test+b0

#plot training data
plt.scatter(x_train,y_train,color='red',label='Training')
plt.scatter(x_test,y_pred,color='blue',label='Prediction')
plt.scatter(x_test,y_test,color='green',label='Actual Values')
plt.show()

sst,ssr=0,0
for i in range(len(y_test)):
    sst+=(y_test[i]-y_test.mean())
    ssr+=(y_test[i]-y_pred[i])**2
R=1-(float(ssr)/float(sst))
print("Score of the linear model:",R)