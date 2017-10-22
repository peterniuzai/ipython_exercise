import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()
ax.plot([0,8],[8,0])
ax.plot([0,5],[8,0])
ax.plot([0,9],[8,0])
ax.plot([0,12],[8,0])
ax.plot([0,16],[8,0])
ax.plot([0,15],[8,0])
ax.plot([0,17],[8,0])

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)
ax.grid(True)
plt.show()

