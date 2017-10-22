import struct
import sys
import numpy as np
import matplotlib.pyplot as plt
num = 1032
if len(sys.argv) == 2:
    num = int(sys.argv[1])

data = open('data.txt', 'rb')
print struct.unpack(num*'B', data.read(num))
b=np.array(struct.unpack(num*'B', data.read(num)))

a=np.array(range(1032))
#print b
plt.plot(a,b,'ro')
plt.xlabel('frequency points')
plt.ylabel('Amplitude')
plt.title('Frequency points after FFT(The former 32 frequency)')
plt.grid()
plt.show()


