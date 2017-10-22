import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
x=np.arange(8)
print x
y=x**2
print y
#ax.plot([0,8],[8,0])
#ax.plot([0,5],[8,0])
ax.plot(x,y)
#ax.plot([0,8],[8,5])
#ax.plot([0,8],[8,1])
ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)
ax.grid(True)
plt.show()

