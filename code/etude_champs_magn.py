import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

from scipy import misc
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Pour r qui se raproche de 0
n = 1000
'''
fig1 = plt.figure()
fig2 = plt.figure()'''
fig3 = plt.figure()
fig4 = plt.figure()
fig5 = plt.figure()
'''
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')'''
ax3 = fig3.gca(projection='3d')
ax4 = fig4.gca(projection='3d')
ax5 = fig5.gca(projection='3d')

r = np.linspace(-11, 11, n)
z = np.linspace(-11, 15, n)
r, z = np.meshgrid(r, z)
'''
coordBr0 = mg.Br0(r, z) 
coordBz0 = mg.Bz0(r, z)'''
coordBr = mg.Br(abs(r), abs(z))
coordBz = mg.Bz(abs(r), abs(z))
coordNorm = mg.normeB(abs(r), abs(z))
'''
planeBr0 = ax1.plot_surface(r, z, coordBr0, label = 'Br0', color = 'b')
planeBz0 = ax2.plot_surface(r, z, coordBz0, label = 'Bz0', color = 'r') '''
planeBr = ax3.plot_surface(r, z, coordBr, label = 'Br', color = 'g')
planeBz = ax4.plot_surface(r, z, coordBz, label = 'Bz', color = 'm')
planeNorm = ax5.plot_surface(r, z, coordNorm, label = 'Norme de B', color = 'y')

plt.show()
#Streamplot et quiver pour les cartes et lignes de champ