import matplotlib.pyplot as plt
import numpy as np
a = np.zeros([1024,1024])
noise = np.random.random(a.shape)
a = a + noise

for n in range(100): 
  for i in range(1024):
    for j in range(1024):
        if j == 2*i+n+10:
            a[i,j]=i*j/10
	    a[i,j]=0
#a[80:200,:]=0
b = np.fft.rfft2(a,norm='ortho')
#b[-1,:]=0
#b[:,0]=0
b[0,0]=0
bb = np.fft.fftshift(b)#,axes=0)
print b.shape
#exit()
#c = b[b.shape[0]/2:,:b.shape[1]/2]+b[:b.shape[0]/2,b.shape[1]/2+1:]

plt.figure(figsize=(35,16))
plt.subplot(2,2,1)
plt.pcolormesh(a)
plt.colorbar()

plt.subplot(2,2,2)
plt.pcolormesh(abs(b))
plt.colorbar()

plt.subplot(2,2,3)
plt.pcolormesh(b.imag)
plt.colorbar()

plt.subplot(2,2,4)
plt.pcolormesh(b.real)
plt.colorbar()
plt.show()
