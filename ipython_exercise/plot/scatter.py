import matplotlib.pyplot as plt
import numpy as np
a	=	np.arange(1,8,2)
b	=	np.ones(4)
x	=	b[:,None]*a[None,:]
x	=	x.reshape(-1)
print x
#exit()
y	=	a[:,None]*b[None,:]
print y
#exit()
x1	=	x + 1
y1	=	y 

plt.scatter(x,y,marker='o',c='1',edgecolor='0',s=50)
plt.scatter(x1,y1,marker='x',s=50)
plt.show()
