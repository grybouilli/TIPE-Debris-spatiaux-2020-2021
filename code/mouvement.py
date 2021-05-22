import etude_alignement as ali
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op
import aimantation as aim
import champ_mag as mag


M_VOL_ALU = 2700 #kg/m^3

HAUTEUR = 0.05
LONGUEUR = 0.05
LARGEUR = 0.05
VOLUME  = HAUTEUR * LONGUEUR*LARGEUR
MASSE_AL = M_VOL_ALU * VOLUME
J_INERTIE = MASSE_AL*(HAUTEUR**2+LONGUEUR**2+LARGEUR**2) / 12


n_al = 0.181/(10**30) #(Ã©lectrons par m^3)


def force_mag(r,z,t,alpha0):
    N_e = n_al * HAUTEUR * LONGUEUR * LARGEUR
    norme_p = aim.norme_M_pop(r,z,N_e)
    
    def angle_moment(rr,zz):
        return ali.alpha(rr,zz,norme_p,J_INERTIE,alpha0,t)   
        
    p_r = lambda rr,zz: np.sin(angle_moment(rr,zz)) * aim.norme_M_pop(rr,zz,N_e)
    p_z = lambda rr,zz: np.cos(angle_moment(rr,zz)) * aim.norme_M_pop(rr,zz,N_e)  
    
    pp_r = p_r(r,z)
    pp_z = p_z(r,z)  
    dp_r_dr , dp_r_dz = op.derive_r(p_r,10**-6)(r,z), op.derive_z(p_r,10**-6)(r,z) 
    dp_z_dr , dp_z_dz = op.derive_r(p_z,10**-6)(r,z), op.derive_z(p_z,10**-6)(r,z)  

    br = mag.Br(r,z)
    bz = mag.Bz(r,z)
    db_r_dr,db_r_dz = op.derive_r(mag.Br,10**-6)(r,z) , op.derive_z(mag.Br,10**-6)(r,z)
    db_z_dr,db_z_dz = op.derive_r(mag.Bz,10**-6)(r,z) , op.derive_z(mag.Bz,10**-6)(r,z)

    cst1_r = (dp_z_dr- dp_r_dz) * bz
    cst1_z = (dp_r_dz - dp_z_dr) * br

    cst2_r = pp_r * db_r_dr + pp_z * db_r_dz
    cst2_z = pp_r * db_z_dr + pp_z * db_z_dz

    cst3_r = br * dp_r_dr + bz * dp_r_dz 
    cst3_z = br * dp_z_dr + bz * dp_z_dz
    return cst1_r + cst2_r + cst3_r, cst1_z + cst2_z + cst3_z

def ac(m, r, z, t, alpha0):
    f_r, f_z = force_mag(r, z, t, alpha0)
    f_r *= (1/m)
    f_z *= (1/m)
    return (f_r, f_z)

def pos_verlet(m, alpha0, p0, tf, n):
    h = tf/n
    V = np.zeros((n, n))
    P = np.zeros((n, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    
    for k in range (1, n) :
        a_r_n, a_z_n = ac(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        P[0][k] = P[0][k-1] + h*V[0][k-1] + ((h**2)/2)*a_r_n
        P[1][k] = P[1][k-1] + h*V[1][k-1] + ((h**2)/2)*a_z_n
        T[k] = T[k-1] + h
        
        a_r_n1, a_z_n1 = ac(m, P[0][k], P[1][k], T[k], alpha0)
        V[0][k] = V[0][k-1] + (h/2)*(a_r_n + a_r_n1)
        V[1][k] = V[1][k-1] + (h/2)*(a_z_n + a_z_n1)
        
    return (P[0], P[1])

'''
w = 11/10 * mg.L

t0 = 0
alpha0 = 0

figb, axb = plt.subplots()

r, z = np.arange(-w, w, 0.2), np.arange(-w, w, 0.2)
r, z = np.meshgrid(r, z)
U, V = np.zeros((len(r), len(r))), np.zeros((len(r), len(r)))

for i in range (len(r)):
    for j in range (len(r)):     
        U[i][j], V[i][j] = force_mag(r[i][j], z[i][j] , t0, alpha0)[0], force_mag(r[i][j], z[i][j], t0, alpha0)[1]

axb.xaxis.set_ticks([])
axb.yaxis.set_ticks([])

axb.quiver(r, z, U, V, alpha=0.5,color='grey')
'''


pos_r, pos_z = pos_verlet(0.1, 0, (0.5, 2), 10, 1000)

plt.plot(pos_r, pos_z, color = 'r')
plt.show()
