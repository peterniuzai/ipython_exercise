from scipy import integrate 
from numpy import sqrt
import matplotlib.pyplot as plt
import numpy as np 
x=np.linspace(0,1.2,num=100) 
y1,y2=x**2,sqrt(x) 
plt.plot(x,y1,'r',x,y2,lw=3) 

ax = plt.gca() 
ax.spines['right'].set_color('blue') 
ax.spines['top'].set_color('red') 
ax.spines['left'].set_color('yellow')
ax.xaxis.set_ticks_position('bottom') 
ax.spines['bottom'].set_position(('data',0)) 
ax.xaxis.set_visible('True')
ax.yaxis.set_ticks_position('left') 
ax.spines['left'].set_position(('data',0)) 
plt.title('Surface integral of closed Area') 

plt.fill_between(x, y1, y2,where=y2>=y1, facecolor='y', interpolate=False) 
plt.text(0.6, 0.2,r'$y_1=x^2$',fontsize=20) 
plt.text(0.05, 0.65,r'$y_2=\sqrt{x}$',fontsize=20,) 
plt.axis([-0.2, 1.2, -0.2, 1.2]) 
plt.grid(True) 
plt.annotate('Area D', xy=(0.3,0.42),fontsize=20) 

plt.ylim(-0.2,1.4) 
plt.xlim(-0.2,1.4) 
plt.yticks([i*0.2 for i in np.arange(1,8)],[r'0.2', r'$0.4$', r'$0.6$', r'$0.8$', r'$1.0$', r'$1.2$', r'$1.4$'],fontsize=10,) 
plt.show() 


s1,abser1 = integrate.quad(lambda x:sqrt(x)-x**2,0,1) 
print("Area of D is %.10f" %s1) 
s2,abser2 = integrate.dblquad(lambda x,y: 1,0,1,lambda x :x**2,lambda x:sqrt(x)) 
print("Area of D is %.10f" %s2) 
