import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('image.jpg')


fCascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
plt.imshow(imGray,cmap="gray")

face=fCascade.detectMultiScale(imGray,1.3,5)



x,y,h,w=face[0]
newFace = image[y:y+h,x:x+w,:]
nfGray=cv2.cvtColor(newFace,cv2.COLOR_BGR2GRAY)
newFaceEdge =cv2.Canny(nfGray,30,200)
plt.imshow(newFaceEdge,cmap="gray")
image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

image=cv2.putText(image,"Scahin",(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL
,1,(0,255,0),2)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

image=cv2.imread('image.jpg')
imGray=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
faces=fCascade.detectMultiScale(imGray,1.15,5)
for face in faces:
    x,y,h,w=face
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))




cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()

    faceGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=fCascade.detectMultiScale(faceGray,1.3,5)
    edges=cv2.Canny(faceGray,30,200)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(edges,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('Video',image)
    if cv2.waitKey(1) ==27:
        cap.release()
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()