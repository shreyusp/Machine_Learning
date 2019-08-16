import cv2
import numpy as np
import matplotlib.pyplot as plt
black=np.zeros((48,48))
black[::4]=255
plt.imshow(black,cmap="gray")
a="abcdefghijklmnopqrstuvwxyx"
cv2.imshow('frame Name', black)
cv2.waitKey(0)