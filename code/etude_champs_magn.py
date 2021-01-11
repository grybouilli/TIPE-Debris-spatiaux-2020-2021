import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

# Pour r qui se raproche de 0
n = 1000
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')
ax3 = fig3.gca(projection='3d')

r = np.linspace(1, 50, n)
z = np.linspace(1, 50, n)
r, z = np.meshgrid(r, z)
coordBr0 = mg.Br0(r, z) 
coordBz0 = mg.Bz0(r, z) 
coordBr = mg.Br(r, z)

planeBr0 = ax1.plot_surface(r, z, coordBr0, label = 'Br', color = 'b')
planeBz0 = ax2.plot_surface(r, z, coordBz0, label = 'Bz', color = 'r') 
planeBr = ax3.plot_surface(r, z, coordBr, label = 'Br', color = 'g')

plt.show()
