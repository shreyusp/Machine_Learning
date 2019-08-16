import cv2
import numpy as np
import matplotlib.pyplot as plt

fCascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceData=[]
faceCount=0
cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()

    faceGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=fCascade.detectMultiScale(faceGray,1.3,5)
    edges=cv2.Canny(faceGray,30,200)
    for (x,y,w,h) in faces:
    
        croppedFace=image[y:y+h,x:x+w,:]
        resizedFace=cv2.resize(croppedFace,(50,50))
        if faceCount%10==0 and len(faceData)<=20:
            faceData.append(resizedFace)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    faceCount+=1
    cv2.putText(image,str(len(faceData)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow('original',image)
    if cv2.waitKey(1) ==27 or len(faceData) >20:
        cap.release()
        #cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()


faceData=np.array(faceData)
np.save('Joy',faceData)