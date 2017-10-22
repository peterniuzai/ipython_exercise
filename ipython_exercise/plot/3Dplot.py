import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax  = Axes3D(fig)
leng= 100
x   = np.arange(leng)
y   = np.arange(leng)
x,y = np.meshgrid(x,y)
z   = np.sin((x+y)*2*np.pi/leng)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
