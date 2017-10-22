import numpy as np
import matplotlib.pyplot as plt

a	=	np.arange(10001)
b	=	np.fft.fft(a)
b	=	np.fft.fftshift(b)
print "Input Array shape:",a.shape
print "Output Array shape:",b.shape
plt.plot(abs(b),'.')
plt.grid()
plt.show()
