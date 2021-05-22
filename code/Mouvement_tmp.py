import mouvement_champ as mv
import matplotlib.pyplot as plt
import aimantation as aim
import Magnétisme as mg
import numpy as np

def const_temps(r, z):
    p = aim.norme_M_pop(r, z, mv.n_al)
    bz = mg.Bz(r, z)
    j = mv.J_INERTIE
    return j/(p*bz)

def accél (m, r,z,t, alpha0):
    f_r, f_z = mv.force_magnetique(abs(r), abs(z), t, alpha0)
    f_r *= (1/m)
    f_z *= (1/m)
    return (f_r, f_z)

def position_euler(m, alpha0, p0, tf, n):
    h = tf/n #pas
    V = np.zeros((2, n)) #vitesse initiale
    P = np.zeros((2, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    for k in range (1, n):
        a_r , a_z = accél(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        V[0][k] = V[0][k-1] + h*a_r
        V[1][k] = V[1][k-1] + h*a_z
        P[0][k] = P[0][k-1] + h*V[0][k-1] #je sais pas si c'est k ou k-1 dans le Y, à vérifier
        P[1][k] = P[1][k-1] + h*V[1][k-1]
        T[k] = k*h
    return (P[0], P[1])

def position_verlet_var(m, alpha0, p0, tf, delta_pos):
    V_r = np.zeros(1)
    V_z = np.zeros(1)
    P_r = np.zeros(1)
    P_z = np.zeros(1)
    P_r[0], P_z[0] = p0
    
    t = 0
    k = 0
    h = 0.01
    
    while t < tf :
        a_r_n, a_z_n = accél(m, P_r[k], P_z[k], t, alpha0)
        P_r = np.append(P_r, P_r[k] + h*V_r[k] + ((h**2)/2)*a_r_n)
        P_z = np.append(P_z, P_z[k] + h*V_z[k] + ((h**2)/2)*a_z_n)
        t += h
#        print("t =", t)        
        
        a_r_n1, a_z_n1 = accél(m, P_r[k+1], P_z[k+1], t, alpha0)
        V_r = np.append(V_r, V_r[k] + (h/2)*(a_r_n + a_r_n1))
        V_z = np.append(V_z, V_z[k] + (h/2)*(a_z_n + a_z_n1))
        
        v = np.sqrt((V_r[k+1])**2 + (V_z[k+1])**2)
#        print("v=", v)
        if v > (delta_pos/tf)*1000 :
            h = delta_pos/v
        else :
            h = tf/100
#        print("h =", h)
        k += 1
    return (P_r, P_z, t)

pos_r, pos_z, t_fin = position_verlet_var(0.1, 0, (0.5, 2), 1000, 0.01)
#pos_r, pos_z = position_euler(0.1, 0.1, (0.5, 3), 100, 10000)
print("t =", t_fin)

plt.plot(pos_r, pos_z, color = 'r')
plt.show()

'''
pas de temps adaptatif

'''
