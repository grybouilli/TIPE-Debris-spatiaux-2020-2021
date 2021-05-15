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


MASSE = 10
HAUTEUR = 5
LONGUEUR = 5
LARGEUR = 5
J_INERTIE = MASSE*(HAUTEUR**2+LONGUEUR**2+LARGEUR**2) / 12



def force_magnetique(r,z,t,alpha0):
    def alpha(rr,zz):
        return al.angle_alpha_moment(rr,zz,t,abs(norme_p),J_INERTIE,alpha0)
        
    norme_p = aim.norme_M(r,z)
    aalpha,thau = alpha(r,z)

    p_r,p_z= lambda r,z : np.sin(alpha(r,z)) * aim.norme_M(r,z), lambda r,z: np.cos(alpha(r,z)) * aim.norme_M(r,z)  #fonctions

    pp_r,pp_z = p_r(r,z),p_z(r,z)   #valeurs numériques

    dp_r_dr , dp_r_dz = op.derive_r(p_r,10**-6)(r,z), op.derive_z(p_r,10**-6)(r,z)  #valeurs numériques
    dp_z_dr , dp_z_dz = op.derive_r(p_z,10**-6)(r,z), op.derive_z(p_z,10**-6)(r,z)  #valeurs numériques

    br = mg.Br(r,z)
    bz = mg.Bz(r,z)
    db_r_dr,db_r_dz = op.derive_r(mg.Br,10**-6)(r,z) , op.derive_z(mg.Br,10**-6)(r,z)   #valeurs numériques
    db_z_dr,db_z_dz = op.derive_r(mg.Bz,10**-6)(r,z) , op.derive_z(mg.Bz,10**-6)(r,z)   #valeurs numériques

    cst1_r = (dp_z_dr- dp_r_dz) * bz
    cst1_z = (dp_r_dz - dp_z_dr) * br

    cst2_r = pp_r * db_r_dr + pp_z * db_r_dz
    cst2_z = pp_r * db_z_dr + pp_z * db_z_dz

    cst3_r = br * dp_r_dr + bz * dp_r_dz 
    cst3_z = br * dp_z_dr + bz * dp_z_dz

    return cst1_r + cst2_r + cst3_r, cst1_z + cst2_z + cst3_z



figr = plt.figure()
figz = plt.figure()
fig = plt.figure()
axr = figr.gca(projection='3d')
axz = figz.gca(projection='3d')
ax = fig.gca(projection='3d')

n = 1000
r = np.linspace(-11, 11, n)
z = np.linspace(-11, 15, n)
r, z = np.meshgrid(r, z)

Fr,Fz = force_magnetique(r,z,0,0)
F = op.norme(Fr,Fz)

planeR = axr.plot_surface(r, z, Fr, label = 'force magnétique sur r', color = 'r')
planeZ = axz.plot_surface(r, z, Fz, label = 'force magnétique sur z', color = 'g')
planeNorme = ax.plot_surface(r, z, F, label = 'force magnétique (norme)', color = 'b')
plt.show()