import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

n = 10000

fig, ax = plt.subplots()

r, z = np.arange(-50, 50), np.arange(-50, 50)
r, z = np.meshgrid(r, z)
U, V = mg.Br(abs(r), abs(z)), mg.Bz(abs(r), abs(z))

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

ax.quiver(r, z, U, V)
ax.set_title('Norme du champ magnétique')
plt.show()
