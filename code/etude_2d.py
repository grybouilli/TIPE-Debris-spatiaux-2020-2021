import champ_mag as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

epsilon = 0
w = 11/10 * mg.L

fig, ax = plt.subplots()

r, z = np.arange(-w, w, 0.05), np.arange(-w, w, 0.05)
r, z = np.meshgrid(r, z)
U, V = np.zeros((len(r), len(r))), np.zeros((len(r), len(r)))
for i in range (len(r)):
    for j in range (len(r)):
        U[i][j], V[i][j] = mg.Br(r[i][j], z[i][j]), mg.Bz(r[i][j], z[i][j])

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

mo = len(U)
moo = len(V)
print("La norme au milieu du champ est",np.sqrt(U[mo//2][mo//2] **2 + V[moo//2][moo//2] **2),"normalement",  mg.mu0 * mg.n * mg.L * mg.intensite)

'''
ax.quiver(r, z, U, V)
'''
#Carte des intensités
ax.set_title('Norme champ magnétique')

#Vecteur champ magnétique
plt.pcolor(z, r, np.sqrt(U**2 + V**2), label = 'Norme du champ magnétique', cmap = 'coolwarm')
plt.colorbar()

plt.show()