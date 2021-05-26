from numpy.core.getlimits import _register_known_types
import etude_alignement as ali
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op
import aimantation as aim
import champ_mag as mag
import mouvement as mv

h = 0.05
l = 0.05
L = 0.05
m = 2700 *h *l *L

r = 10
z = 1
n_al = 0.181*(10**30)
N = n_al * h * l * L
moment_p = aim.norme_M_pop(r,z,N)
J = m*(h**2+l**2+L**2) / 12

def cherche_liste(L, x, epsilon):
    index = 0
    compteur = 0
    for i in range(10, len(L)- 1):
        if np.abs(x - L[i]) <= epsilon and compteur == 0:
            compteur += 1
        if np.abs(x - L[i]) <= epsilon and compteur == 1:
            index = i
    return index

def cherche_min(L):
    min = L[0]
    for e in L:
        if e < min:
            min = e
    return min


#Trouve la plus petite période d'oscillation pour réduire les calculs tout en étant dans l'approx de l'angle constant
def cherche_pulsation():
    alpha0 = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]
    angle = []

    for al0 in alpha0:
        al, T = ali.alpha_reel(r, z, moment_p, J, al0, 9000, 10000)
        angle.append(al)
        temps = T
    
    Tc = []

    for i in range(len(angle)):
        Tc.append(cherche_liste(angle[i], alpha0[i], 10**(-5)))
    
    periode = []
    for t in Tc:
        periode.append(temps[t])

    return cherche_min(periode)

#Le temps de l'étude, dans lequel on considère l'angle constant
t_app = cherche_pulsation()/10


def compris(x, lim1, lim2):
    return x >= lim1 and x <= lim2

def trouve_capture(m, alpha0, p0, tf, n):
    rg, rb = -1, 1   #limites en r de la moitie basse du solenoide
    zb, zh = -1.5, 0 #limites en z de la moitie basse du solenoide
    h = tf/n #pas
    V = np.zeros((2, n)) #vitesse initiale
    P = np.zeros((2, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    for k in range (1, n):
        a_r , a_z = mv.ac(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        V[0][k] = V[0][k-1] + h*a_r
        V[1][k] = V[1][k-1] + h*a_z
        P[0][k] = P[0][k-1] + h*V[0][k-1] #je sais pas si c'est k ou k-1 dans le Y, à vérifier
        P[1][k] = P[1][k-1] + h*V[1][k-1]
        if compris(P[0][k], rg, rb) and compris(P[1][k], zb, zh):
            return True
        T[k] = k*h
    return False

r1, z1 = np.arange(-1.5, 1.6, 1), np.arange(1.5, 4.6, 1)
r1, z1 = np.meshgrid(r1, z1)

def liste_points_cap():
    r_cap = []
    z_cap = []
    r_nope = []
    z_nope = []

    for i in range(len(r1)):
        for j in range(len(r1[0])):
            if trouve_capture(0.1, 0.1, (r1[i][j], z1[i][j]), t_app, 50):
                r_cap.append(r1[i][j])
                z_cap.append(z1[i][j])
            else:
                r_nope.append(r1[i][j])
                z_nope.append(z1[i][j])

    return r_cap, z_cap, r_nope, z_nope

print(r1, z1)

plt.figure()

plt.vlines(x = [-1, 1], ymin = [-1.5, -1.5], ymax = [1.5, 1.5], colors = 'teal')
plt.hlines(y = 1.5, xmin = -1, xmax = 1, colors = 'teal')
plt.hlines(y = -1.5, xmin = -1, xmax = 1, colors = 'teal')

r_cap, z_cap, r_nope, z_nope = liste_points_cap()
for i in range(len(r_cap)):
    plt.plot(r_cap[i], z_cap[i], color = 'red', marker = '+', markersize = 12)
for i in range(len(r_nope)):
    plt.plot(r_nope[i], z_nope[i], color = 'blue', marker = '+', markersize = 12)

plt.show()
