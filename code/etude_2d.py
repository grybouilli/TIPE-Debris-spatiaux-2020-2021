import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

n = 10000
epsilon = 0.001
fig, ax = plt.subplots()

r, z = np.arange(-50, 50), np.arange(-50, 50)
r, z = np.meshgrid(r, z)
U, V = mg.Br_aj(abs(r), abs(z), epsilon), mg.Bz_aj(abs(r), abs(z), epsilon)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

ax.quiver(r, z, U, V)
ax.set_title('Norme du champ magnétique')
plt.show()
