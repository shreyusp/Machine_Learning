import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('lena.jpg')

fcascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
plt.imshow(imGray,cmap="gray")

face=fcascade.detectMultiScale(imGray,1.3,5)

lel=image[114:400,111:400,:]
plt.imshow(lel)