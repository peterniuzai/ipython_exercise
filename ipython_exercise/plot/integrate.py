import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def calculate(x):
      return (np.exp(1j*x)+np.exp(-1j*x))*np.exp(-1j*x)/2
x=np.linspace(-3,3,1000)
a,err = integrate.quad(calculate,-np.inf,np.inf)
print 'result:',a
print 'err',err
plt.plot(x,calculate(x))
plt.show()
