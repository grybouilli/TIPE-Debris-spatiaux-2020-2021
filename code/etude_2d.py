import Magnétisme as mg
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()

ax1 = fig1.gca(projection='3d')
ax2 = fig2.gca(projection='3d')
ax3 = fig3.gca(projection='3d')

r = np.linspace(1, 11, n)
z = np.linspace(1, 15, n)
r, z = np.meshgrid(r, z)

coordBr = mg.Br(r, z)
coordBz = mg.Bz(r, z)
coordNorm = mg.normeB(r, z)