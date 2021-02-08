import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

n = 10000
epsilon = 0
w = 11

fig, ax = plt.subplots()

r, z = np.arange(-w, w, 0.1), np.arange(-w, w, 0.1)
r, z = np.meshgrid(r, z)
U, V = mg.Br_aj(r, z, epsilon), mg.Bz_aj(r, z, epsilon)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])


ax.quiver(r, z, U, V)
'''
ax.set_title('Norme du champ magnétique')
'''
plt.pcolor(z, r, mg.normeB(abs(r), z), label = 'Norme du champ magnétique')

plt.show()
