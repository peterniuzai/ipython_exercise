import numpy as np
import time
import matplotlib.pyplot as plt
t	= []
size	= np.arange(512,1024*20,512)
for i in size:
	x_size = 1024
	y_size = i

	a	= np.random.random([x_size,y_size])
	t1	= time.time()
	for i in range(int(4485120/i/5)):
		b	= np.fft.fft2(a)
	t2	= time.time()
	cost	= t2 - t1
	t.append(cost)

plt.plot(size,t)
plt.grid()
plt.savefig('FFT_speed')
plt.show()
