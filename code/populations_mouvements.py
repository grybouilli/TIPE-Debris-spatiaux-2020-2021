import mouvement as mvt
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op
import champ_mag as mag


#première phase de test pour savoir quoi étudier exactemet et comment présenter les résultats

def calcul_verlet_collision(m, alpha0, p0, tf, n,a_range=[-mag.a,mag.a],L_range=[-mag.L/2,mag.L/2]):
    h = tf/n
    V = np.zeros((n, n))
    P = np.zeros((n, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    for k in range (1, n) :
        a_r_n, a_z_n = mvt.ac(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        
        P[0][k] = P[0][k-1] + h*V[0][k-1] + ((h**2)/2)*a_r_n
        P[1][k] = P[1][k-1] + h*V[1][k-1] + ((h**2)/2)*a_z_n
        
        T[k] = T[k-1] + h
        
        a_r_n1, a_z_n1 = mvt.ac(m, P[0][k], P[1][k], T[k], alpha0)
        V[0][k] = V[0][k-1] + (h/2)*(a_r_n + a_r_n1)
        V[1][k] = V[1][k-1] + (h/2)*(a_z_n + a_z_n1)
        if P[0][k] < a_range[0] or P[0][k] > a_range[1]:
            if L_range[1] >= P[1][k] >= L_range[0]:
                return 1

    return 0

r_init = np.arange(0.6, 1.2, 0.05)
z_init = np.arange(2.8,3.4,0.05)

nr,nz =len(r_init), len(z_init)

file = open("/home/grybouilli/TIPE-Debris-spatiaux-2020-2021/code/population2.txt","w")
file.write("Population faite pour:\n r variant de 0.6 à 1.2, \net z allant de 2.8 à 3.4,\n avec un pas de 0.1,\n une masse de 0.1, \n tf = 200, \n n = 600 \n\n")

for r in r_init:
    for z in z_init:
        a0 = mag.Br(r,z) / mag.Bz(r,z)
        res = calcul_verlet_collision(0.1, a0, (r,z), 200, 600)
        print(res)
        file.write(str(res))
    file.write('\n')

file.close()