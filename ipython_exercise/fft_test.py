import matplotlib.pyplot as plt
import numpy as np

#x = np.zeros([1024,4096])
x = np.random.normal(loc = 0, scale = 1, size = [1024,4096])
count = 0
Pwidth = 15
for i in range(x.shape[1]):
	for j in range(Pwidth):
		if (i - j >0):# and (0<i/5<1024):
	#		x[i,i]= 1
			x[int(i/5),i-(j)] = 0.5
			count = count + 1
#			x[(i-(j))/0.5,i]=1#5*j+5
		



#x[-45:,-45:]=0
#x[10:15,10:15] = 0
print '\ncount',count,'\n'
b = np.fft.fft2(x)
b = np.fft.fftshift(b)
b = b/np.sqrt(b.size)
c = b[1:b.shape[0]/2+1,b.shape[1]/2:]

#ang_rsl = np.arctan(1./c.shape[1])*180/np.pi
ang_rsl	= 0.1
print "Angle resolution:",ang_rsl,"Degree"

rang   = c.shape
row    = np.arange(-rang[0]+1,1,dtype=np.float32)
rank   = np.arange(rang[1],dtype=np.float32)
#row    = np.arange(-rang[0]+2,2,dtype=np.float32)
#rank   = np.arange(1,rang[1]+1,dtype=np.float32)
angle  = (np.nan_to_num(np.arctan(row[:,None]/rank[None,:]))/ np.pi * 180)
print angle.shape,angle.dtype
#exit()
ang	= -angle.reshape(-1)
#ang     = np.int64(ang)

data   	= c.reshape(-1)
#d	= np.bincount(ang,  weights=abs(data))
print 'start?'
d,bin_eage  = np.histogram(ang,  weights=data, bins = np.arange(1,88,ang_rsl))#,density =True)
print d.dtype
print 'end?'
print c.shape
#d	= d*4
#d	= np.imag(d) + np.real(d)
print '\n***Max,Std,SNR***'
print 'Real Part:',np.max(d.real),np.std(d.real)
print 'Imag Part:',np.max(d.imag),np.std(d.imag)
print 'Abs  Part:',np.max(np.abs(d)),np.std(np.abs(d))
print '*************\n'
d	= np.abs(d)
#d	= np.imag(d)
SNR	= (d.max()-d.mean())/d.std()
print 'SNR:',SNR

plt.figure(figsize = [17,14])
plt.subplot(2,2,1)
plt.pcolormesh(x)
plt.colorbar()



plt.subplot(2,2,2)
plt.pcolormesh(np.abs(b))
plt.colorbar()

plt.subplot(2,2,3)
plt.pcolormesh(abs(c))
plt.colorbar()

plt.subplot(2,2,4)
plt.grid()
plt.plot(d)

plt.show()
