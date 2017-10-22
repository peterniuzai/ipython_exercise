import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(2,2,sharex=True,sharey=True)
ax[0,0].plot([0,1],[1,7],'-')
ax[0,1].plot([8,1],[1,7],'-')
#ax[1,1].plot([8,1],[1,7],'-')
#ax3=fig.add_subplot(2,1,2)
ax3 = plt.subplot(2,2,4)
ax3.plot([1,2],[3,4],'-')
#print ax3.shape
plt.show()
