import Magnétisme as mg
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np
import etude_alignement as al
import operateurs_vectoriels as op
from scipy import misc
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import librairies.display as disp
import matplotlib as mpl

M_VOL_ALU = 2700 #kg/m^3


HAUTEUR = 0.5
LONGUEUR = 0.5
LARGEUR = 0.5
VOLUME  = HAUTEUR * LONGUEUR*LARGEUR
MASSE_AL = M_VOL_ALU * VOLUME
J_INERTIE = MASSE_AL*(HAUTEUR**2+LONGUEUR**2+LARGEUR**2) / 12

n_al = 0.181/(10**-30) #(électrons par m^3)
n_zn = 0.143/(10**-30)
n_ti = 0.043/(10**-30)

N_e_al = n_al * VOLUME
N_e_zn = n_zn * VOLUME
N_e_ti = n_ti * VOLUME


n = 1000
r = np.linspace(-11, 11, n)
z = np.linspace(-11, 15, n)
r, z = np.meshgrid(r, z)

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
M_al = aim.norme_M_pop(abs(r),z,N_e_al)
M_zn = aim.norme_M_pop(abs(r),z,N_e_zn)
M_ti = aim.norme_M_pop(abs(r),z,N_e_ti)

ax1.set_xlabel("r")
ax1.set_ylabel("z")
ax1.set_zlabel("Aimantation (A.m^2)")

ax1.plot_surface(r,z,M_al,alpha=0.25, color='m')
ax1.plot_surface(r,z,M_zn, alpha=0.5, color='g')
ax1.plot_surface(r,z,M_ti, color='b')

al = mpl.lines.Line2D([0],[0], linestyle="none", c='m', marker = 'o')
zn = mpl.lines.Line2D([0],[0], linestyle="none", c='g', marker = 'o')
ti = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
ax1.legend([al,zn,ti], ['Aluminium','Zinc','Titane'], numpoints = 1)
plt.show()