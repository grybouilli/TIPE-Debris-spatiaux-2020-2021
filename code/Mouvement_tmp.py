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
    p = p0
    y = (0,0) #vitesse initiale
    t = 0
    P = [p0]
    T = [0]
    for k in range (n):
        a_r , a_z = accél(m, p[0], p[1], t, alpha0)
        y = (y[0] + h*a_r, y[1] + h*a_z)
        p = (p[0] + h*y[0], p[1] + h*y[1])
        
        t += h
        P.append(p)
        T.append(t)
    print(P)
    pos_r = [e[0] for e in P]
    pos_z = [e[1] for e in P]
    return (pos_r, pos_z, T)

pos_r, pos_z, T = position(0.1, 0.1, (1.5, 0), 10, 100)
print(pos_r)
print(pos_z)

    