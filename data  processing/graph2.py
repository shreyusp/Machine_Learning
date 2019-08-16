import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11)
y=x**4
z=2*x+3
plt.subplot(121)
plt.plot(x,y,'r-o',label='first')
plt.subplot(122)
plt.plot(x,y,'b-o',label='second')
plt.legend()
plt.title("graph1")
plt.xlabel("graph2")
plt.show()