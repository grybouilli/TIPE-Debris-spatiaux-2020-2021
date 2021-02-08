import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

epsilon = 0
w = 11

fig, ax = plt.subplots()

r, z = np.arange(-w, w, 0.3), np.arange(-w, w, 0.3)
r, z = np.meshgrid(r, z)
U, V = mg.Br_aj(r, z, epsilon), mg.Bz_aj(r, z, epsilon)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

mo = len(U)
moo = len(V)
print("La norme au milieu du champ est",np.sqrt(U[mo//2][mo//2] **2 + V[moo//2][moo//2] **2),"normalement",  mg.mu0 * mg.n * mg.L * mg.i )

ax.quiver(r, z, U, V)
#Carte des intensités
#ax.set_title('Norme du champ magnétique')

#Vecteur champ magnétique 
#plt.pcolor(z, r, mg.normeB(abs(r), z), label = 'Norme du champ magnétique')

#plt.show()
