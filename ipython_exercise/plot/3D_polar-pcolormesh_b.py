import numpy as np
from matplotlib import pyplot as plt 
import matplotlib.cm as cm 
from scipy import integrate

Z = 1
a_0 = 1
pi = np.pi


n = 300
r = np.linspace(0, 10, n) 
theta = np.linspace(0, 2*pi, n) 
R, Theta = np.meshgrid(r, theta) 

def psi(r,theta):
    return 1/(4*np.sqrt(2*pi))*(Z/a_0)**(3/2) * Z*r/a_0*np.exp(-Z*r/(2*a_0))*np.cos(theta)


X1 = R*np.cos(Theta)
X2 = R*np.sin(Theta)
print 'X1 shape:',X1.shape,psi(R,Theta).shape
plt.pcolormesh(X1,X2,psi(R,Theta)**2)
plt.colorbar()
plt.axis('equal')
plt.show()
