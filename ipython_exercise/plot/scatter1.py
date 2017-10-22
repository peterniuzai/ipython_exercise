import matplotlib.pyplot as plt
import numpy as np
x	=	np.array([1,3,5,2,4,1,3,5,2,4,1,3,5,2,4,1,3,5,2,4,1,3,5,2,4])
y	=	np.array([2,2,2,1,1,4,4,4,3,3,6,6,6,5,5,8,8,8,7,7,10,10,10,9,9])
print y
#exit()
#x1	=	np.array([1,3,5,2,4,1,3,5,2,4,1,3,5,2,4,1,3,5,2,4,1,3,5,2,4])
#y1	=	np.array([2,2,2,1,1,4,4,4,3,3,6,6,6,5,5,8,8,8,7,7,10,10,10,9,9])
x1	= x
y1	= y +1
plt.scatter(x,y,marker='o',c='1',edgecolor='0',s=50)
plt.scatter(x1,y1,marker='x',s=50)
ax	=	plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
plt.title('Array postion to do 3D FFT')

plt.show()
