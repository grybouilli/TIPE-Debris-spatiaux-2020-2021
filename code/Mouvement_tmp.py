import mouvement_champ as mv
import matplotlib.pyplot as plt
import numpy as np

def accél (m, r,z,t, alpha0):
    f_r, f_z = mv.force_magnetique(abs(r), abs(z), t, alpha0)
    f_r *= (1/m)
    f_z *= (1/m)
    return (f_r, f_z)

def position(m, alpha0, p0, tf, n):
    h = tf/n #pas
    Y = np.zeros((2, n)) #vitesse initiale
    P = np.zeros((2, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    for k in range (1, n):
        a_r , a_z = accél(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        Y[0][k] = Y[0][k-1] + h*a_r
        Y[1][k] = Y[1][k-1] + h*a_z
        P[0][k] = P[0][k-1] + h*Y[0][k-1] #je sais pas si c'est k ou k-1 dans le Y, à vérifier
        P[1][k] = P[1][k-1] + h*Y[1][k-1]
        T[k] = k*h
    return (P[0], P[1], T)


pos_r, pos_z, T = position(0.1, 0.1, (0.5, 3), 0.01, 10000)
print(pos_r)
print(pos_z)

plt.plot(pos_r, pos_z)
plt.show()

'''
pas de temps addaptatif

améliorer euler
 --> verlet par ex

carte de champ // lignes de champ ??
'''
