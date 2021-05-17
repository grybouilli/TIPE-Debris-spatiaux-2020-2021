#on va essayer de casser nos ordis lol
import mouvement_champ as mvt
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op
from scipy import misc
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import librairies.display as disp

n = 500

r = np.linspace(-5, 5, n)
z = np.linspace(-5, 5, n)
r, z = np.meshgrid(r, z)

Fr,Fz = mvt.force_magnetique(abs(r),abs(z),0,0)
F = op.norme(Fr,Fz)


plt.figure()
#ax = plt.gca()
im = plt.pcolor(r,z,F)
plt.colorbar(im)
for i in range(1, n, 10):
    Fr,Fz = mvt.force_magnetique(abs(r),abs(z),i,0)
    F = op.norme(Fr,Fz)
    plt.pcolor(r,z,F, vmin=0, vmax = 10**5)
    plt.pause(0.01)
    
plt.show()