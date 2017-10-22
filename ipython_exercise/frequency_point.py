import struct
import sys
import numpy as np
import matplotlib.pyplot as plt
num = 1032
if len(sys.argv) == 2:
    num = int(sys.argv[1])

data = open('data.txt', 'rb')
#print struct.unpack(num*'B', data.read(num))
b=np.array(struct.unpack(num*'B', data.read(num)))
#print b
for ind in range(len(b)-8):#  remove the FID XID
   b[ind]=b[ind+8]
for i in range(len(b)):
   if b[i] != 0:
#     print b[i]
     if (b[i] & 0b11110000):
       print "the %d points has value %d,it is in the (%d) of 0~31 frequency points,No.%d of (0~31) channel " % (i,b[i],i/32,i%32/2)
     if (b[i] & 0b00001111):
       print "the %d points has value %d,it is in the (%d) of 0~31 frequency points,No.%d of (0~31) channel " % (i,b[i],i/32,i%32/2+8)

# if b[i]:
  # print i/32
 
#a=np.array(range(1032))
#print b
#plt.plot(a,b,'ro')
#plt.xlabel('frequency points')
#plt.ylabel('Amplitude')
#plt.title('Frequency points after FFT(The former 32 frequency)')
#plt.grid()
#plt.show()


