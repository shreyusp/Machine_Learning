import cv2
import numpy as np
import matplotlib.pyplot as plt

fCascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
names={0:'Kai',1:'Joy'}
person1=np.load("Kai.npy").reshape(21,50*50*3)
person2=np.load("Joy.npy").reshape(21,50*50*3)
data=np.concatenate([person1,person2])
labels=np.zeros((42,1))#one col of 42 entries, all items in label are zeroes
labels[21:,:]=1

'''
from sklearn.preprocessing import LabelEncoder
lencoder=LabelEncoder()
x[:,0]=lencoder.fit_transform(x[:,0])

from sklearn.preprocessing import StandardScaler
sscaler=StandardScaler()
x=sscaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=0)

'''
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(data,labels)
#ypred=clf.predict(x_test)



#take user face
cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    imGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=fCascade.detectMultiScale(imGray,1.3,5)
    for (x,y,w,h) in faces:
    
        croppedFace=image[y:y+h,x:x+w,:]
        resizedFace=cv2.resize(croppedFace,(50,50))
        reshapedFace=resizedFace.reshape(1,50*50*3)
        pred=clf.predict(reshapedFace)
        name=names[int(pred)]
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image,name,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
    cv2.imshow("output",image)
    if cv2.waitKey(1) ==27:
        cap.release()
        #cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()

     

    