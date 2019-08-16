import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('lena.jpg')
imageGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imRed=image[:,:,2]
imBlue=image[:,:,0]
plt.subplot(2,2,1)
plt.imshow(imRed,cmap='gray')
plt.title("Red Component")
plt.subplot(2,2,2)
plt.imshow(imBlue,cmap='gray')
plt.title("Blue Component")
plt.subplot(2,2,3)
plt.imshow(image[:,:,1],cmap='gray')
plt.title("Green Component")
plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title("Original")
LOGO=cv2.imread("logo.jpg",-1)
plt.imshow(LOGO)

newImage=image+LOGO
plt.imshow(cv2.cvtColor(newImage,cv2.COLOR_BGR2RGB))
face=image[114:400,111:400,:]
plt.imshow(face)

cap=cv2.VideoCapture(0)
ret,img=cap.read()
cap.release()
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

r,c,l=img.shape
output=np.zeroes((r,c))
rMax=255
rMin=250
gMax=0
gMin=360
bMax=200
bMin=100

for i in range(0,r):
    for j in range(0,c):
        if img[i,j,0]<bMax and img[i,j,0]>bMin and img[i,j,0]<gMax and img[i,j,0]>gMin and img[i,j,0]<rMax and img[i,j,0]>rMin:
            output[i,j]=255
        else:
            
'''plt.subplot(1,2,1)
plt.imshow(imageGray,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

#cv2.imshow('title',image)
#cv2.waitKey(0)'''