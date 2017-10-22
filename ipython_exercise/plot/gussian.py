import numpy as np
import matplotlib.pyplot as plt
x	=	np.linspace(-100,100,1000)
start1	=	0
start2	=	40
start3	=	-50
sigma	=	15
a	=	0.002
y	=	sigma**-1*(2*np.pi)**-0.5*np.exp(-(x-start1)**2/2./sigma**2) +a
y1	=	sigma**-1*(2*np.pi)**-0.5*np.exp(-(x-start2)**2/2./sigma**2)*0.8 +a
y2	=	sigma**-1*(2*np.pi)**-0.5*np.exp(-(x-start3)**2/2./sigma**2)*0.7 +a
plt.plot(x,y,label='Original beam')
plt.plot(x,y1,label='New beam')
plt.plot(x,y2,label='New beam')
an	=	np.arange(-100,100,20)
pos	=	np.ones(len(an))*0
plt.plot(an,pos,'ro',markersize=15),#label='antenna')
#plt.plot([-100,100],[0,0])
plt.legend(loc='best',prop={'size':8})
ax	=	plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
plt.show()
