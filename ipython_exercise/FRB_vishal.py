import numpy as np
import matplotlib.pyplot as plt

#data	=	np.loadtxt('dedisperse_DM557_scan11_unclib.ascii')
data	=	np.load('Repeated_FRB.npy')



tx	=	data[:,0]
Inten	=	data[:,1]
mean    =       data.mean()
sig     =       data.std()
lo      =       np.where(Inten < -500)
Inten[lo]=	0
plt.plot(tx,Inten)
plt.ylim(-2000,Inten.max())
#time_l	=	[16.252229,263.415224,285.463631,323.381188,344.799052,356.064952,461.836212,580.683213,597.667348,691.892038,704.129619,769.934404,841.012128,993.338764,1036.519473,1142.513380,1454.681446,1789.513084]
time_l =       [16.252229,263.415224,285.463631,323.381188,344.799052,356.064952,461.836212,580.683213,597.667348,691.892038,704.129619,769.934404,841.012128,993.338764,1036.519473,1142.513380,1454.681446,1789.513084]
time_l	= np.array(time_l)
SNR_l	=	[55.75608+-18,7.07,9.99,37.05,28.24,29.17,6.44,7.57,58.03,13.39,9.98,13.90,8.43,11.14,12.42,12.08,20.98,7.43]
name_l	=	['11A','11B','11C','11D','11E','11F','11G','11H','11I','11J','11K','11L','11M','11N','11O','11P','11Q','11R']
#print tx.max(),tx.min()
#print tx[1]-tx[0]
for i in range(18):
	tstamp	=	time_l[i]
	SNR	=	SNR_l[i]
	name	=	name_l[i]
	lo      =       np.where(tx  == tstamp)
	value	=	Inten[lo[0]]
	print 'SNR,name,value',SNR,name,value
#	if i == []
	if i in [2,4,7,9]:

		cord	=	(tstamp,-400)	
		t_cor	= 	(tstamp-25,-500-400-200)
	else:
		cord    =       (tstamp,-400)   
                t_cor   =       (tstamp-25,-500-400)
	plt.annotate(name, xy = cord, xytext = t_cor,
                  arrowprops = dict(arrowstyle="<-",color='0.5'))#,connectionstyle="angle,angleA=-90,angleB=0,rad=0"))

plt.savefig('FRB_positon')
plt.show()
print data.shape
