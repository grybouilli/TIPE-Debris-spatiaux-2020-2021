from code.Magnétisme import Bz
from code.operateurs_vectoriels import derive_r, derive_z
from code.etude_alignement import angle_alpha_moment
from code.aimantation import norme_M
import Magnétisme as mg
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np
import etude_alignement as al
import operateurs_vectoriels as op

MASSE = 10
HAUTEUR = 5
LONGUEUR = 5
LARGEUR = 5
J_INERTIE = MASSE*(HAUTEUR**2+LONGUEUR**2+LARGEUR**2) / 12



def force_magnetique(r,z,t,alpha0):
    def alpha(r,z):
        return al.angle_alpha_moment(r,z,t,norme_p,J_INERTIE,alpha0)
        
    norme_p = aim.norme_M(r,z)
    aalpha,thau = al.angle_alpha_moment(r,z,t,norme_p,J_INERTIE,alpha0)

    p_r,p_z= lambda r,z : np.sin(alpha(r,z)) * aim.norme_M(r,z), lambda r,z: np.cos(alpha(r,z)) * aim.norme_M(r,z)  #fonctions

    pp_r,pp_z = p_r(r,z),p_z(r,z)   #valeurs numériques

    dp_r_dr , dp_r_dz = derive_r(p_r)(r,z), derive_z(p_r)(r,z)  #valeurs numériques
    dp_z_dr , dp_z_dz = derive_r(p_z)(r,z), derive_z(p_z)(r,z)  #valeurs numériques

    br = mg.Br(r,z)
    bz = mg.Bz(r,z)
    db_r_dr,db_r_dz = derive_r(mg.Br)(r,z) , derive_z(mg.Br)(r,z)   #valeurs numériques
    db_z_dr,db_z_dz = derive_r(mg.Bz)(r,z) , derive_z(mg.Bz)(r,z)   #valeurs numériques

    cst1_r = (dp_z_dr- dp_r_dz) * bz
    cst1_z = (dp_r_dz - dp_z_dr) * br

    cst2_r = pp_r * db_r_dr + pp_z * db_r_dz
    cst2_z = pp_r * db_z_dr + pp_z * db_z_dz

    cst3_r = br * dp_r_dr + bz * dp_r_dz 
    cst3_z = br * dp_z_dr + bz * dp_z_dz

    return cst1_r + cst2_r + cst3_r, cst1_z + cst2_z + cst3_z