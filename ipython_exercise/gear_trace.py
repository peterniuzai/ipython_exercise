import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5.1,0.1)
y = np.sqrt(25-x**2)
plt.plot(x,y)
plt.plot(x,-y)
plt.show()
