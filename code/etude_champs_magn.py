import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

#toutes les distances en m
n = 1000
fig1 = plt.figure()
fig2 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')

r = np.linspace(0, 50, n)
z = np.linspace(0, 50, n)
r, z = np.meshgrid(r, z)
coordBr = mg.Br(r, z) 
coordBz = mg.Bz(r, z) 


planeBr = ax1.plot_surface(r, z, coordBr, label = 'Br', color = 'b')
planeBz = ax2.plot_surface(r, z, coordBz, label = 'Bz', color = 'r') 

fig1.colorbar(planeBr, aspect = 5)
fig2.colorbar(planeBz, aspect = 5)
plt.show()
