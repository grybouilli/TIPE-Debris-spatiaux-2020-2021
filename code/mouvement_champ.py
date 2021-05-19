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


M_VOL_ALU = 2700 #kg/m^3

HAUTEUR = 0.5
LONGUEUR = 0.5
LARGEUR = 0.5
VOLUME  = HAUTEUR * LONGUEUR*LARGEUR
MASSE_AL = M_VOL_ALU * VOLUME
J_INERTIE = MASSE_AL*(HAUTEUR**2+LONGUEUR**2+LARGEUR**2) / 12


n_al = 0.181/(10**-30) #(électrons par m^3)

def force_magnetique(r,z,t,alpha0):
    def alpha(rr,zz):
        return al.alpha_reel(rr,zz,abs(norme_p),J_INERTIE,alpha0, t, 1000)[0][-1]   
    N_e = n_al * HAUTEUR * LONGUEUR * LARGEUR
    norme_p = aim.norme_M_pop(r,z,N_e)

    p_r = lambda rr,zz: np.sin(alpha(rr,zz)) * aim.norme_M_pop(r,z,N_e)
    p_z = lambda rr,zz: np.cos(alpha(rr,zz)) * aim.norme_M_pop(r,z,N_e)  
    
    pp_r = p_r(r,z)
    pp_z = p_z(r,z)  
    dp_r_dr , dp_r_dz = op.derive_r(p_r,10**-6)(r,z), op.derive_z(p_r,10**-6)(r,z) 
    dp_z_dr , dp_z_dz = op.derive_r(p_z,10**-6)(r,z), op.derive_z(p_z,10**-6)(r,z)  

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



""" figr = plt.figure()
figz = plt.figure()
fig = plt.figure()
axr = figr.gca(projection='3d')
axz = figz.gca(projection='3d') 
ax = fig.gca(projection='3d')"""

n = 1000
r = np.linspace(-5, 5, n)
z = np.linspace(-5, 5, n)
r, z = np.meshgrid(r, z)
""" 
Fr,Fz = force_magnetique(abs(r),abs(z),0,0)
F = op.norme(Fr,Fz)
planeR = axr.plot_surface(r, z, Fr, label = 'force magnétique sur r', color = 'r')
planeZ = axz.plot_surface(r, z, Fz, label = 'force magnétique sur z', color = 'g') 
planeNorme = ax.plot_surface(r, z, F, label = 'force magnétique (norme)', color = 'b')
plt.show() """

w = 11/10 * mg.L



t = 0
alpha0 = 0


figb, axb = plt.subplots()
r, z = np.arange(-w, w, 0.1), np.arange(-w, w, 0.1)
r, z = np.meshgrid(r, z)
U, V = force_magnetique(abs(r),abs(z),t,alpha0)[0], force_magnetique(abs(r),abs(z),t,alpha0)[1]

axb.xaxis.set_ticks([])
axb.yaxis.set_ticks([])

axb.quiver(r, z, U, V)
