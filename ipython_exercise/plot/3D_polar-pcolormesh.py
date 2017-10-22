import numpy as np
from matplotlib import pyplot as plt 
import matplotlib.cm as cm 
from scipy import integrate



pi	= np.pi
d	= np.load('fft.npy')
#d	= d.reshape

#r = np.linspace(0, 10, n) 
r	= np.load('rad.npy')

ang	= np.load('ang.npy')
print r.shape,ang.shape
ang	= ang/180.*pi
#theta = np.linspace(0, 2*pi, n) 

#R, Theta = np.meshgrid(r, ang) 

#def psi(r,theta):
#    return 1/(4*np.sqrt(2*pi))*(Z/a_0)**(3/2) * Z*r/a_0*np.exp(-Z*r/(2*a_0))*np.cos(theta)



#X1 = r*np.cos(ang)
#X2 = r*np.sin(ang)
print d.shape
ang =ang.reshape(256,256)
r  = r.reshape(256,256)
#X1 = r*np.cos(ang)
#X2 = r*np.sin(ang)
plt.pcolormesh(ang,r,abs(d))
plt.colorbar()
#plt.axis('equal')
plt.show()
