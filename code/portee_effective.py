from numpy.core.getlimits import _register_known_types
import etude_alignement as ali
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op
import aimantation as aim
import champ_mag as mag
import mouvement as mv

hauteur = 0.05
largeur = 0.05
Longueur = 0.05
m = 2700 *hauteur *largeur *Longueur

r = 10
z = 1
n_al = 0.181*(10**30)
N = n_al * hauteur * largeur * Longueur
moment_p = aim.norme_M_pop(r,z,N)
J = m*(hauteur**2+largeur**2+Longueur**2) / 12

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

print(t_app)
def compris(x, lim1, lim2):
    return x >= lim1 and x <= lim2

def choc(r, z):
    A = mag.a
    L1 = mag.L
    #On considère un choc si le centre de masse du débris est a h/2 d'un bord du solénoide
    if (compris(r, -A - hauteur/2, -A + hauteur/2) or compris(r, A - hauteur/2, A + hauteur/2)) and compris(z, -L1/2 - hauteur/2, L1/2 + hauteur/2):
        return True
    if compris(r, -A - hauteur/2, A + hauteur/2) and compris(z, -L1/2 - hauteur/2, -L1/2 + hauteur/2):
        return True
    return False

def trouve_capture(m, alpha0, p0, tf, n):
    rg, rb = -mag.a, mag.a   #limites en r de la moitie basse du solenoide
    zb, zh = -mag.L/2, 0     #limites en z de la moitie basse du solenoide
    h = tf/n #pas
    V = np.zeros((2, n)) #vitesse initiale
    P = np.zeros((2, n))
    P[0][0], P[1][0] = p0
    if choc(P[0][0], P[1][0]):
        return 2
    if compris(P[0][0], rg, rb) and compris(P[1][0], zb, zh):
        return 1
    T = np.zeros(n)
    for k in range (1, n):
        a_r , a_z = mv.ac(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        V[0][k] = V[0][k-1] + h*a_r
        V[1][k] = V[1][k-1] + h*a_z
        P[0][k] = P[0][k-1] + h*V[0][k-1] #je sais pas si c'est k ou k-1 dans le Y, à vérifier
        P[1][k] = P[1][k-1] + h*V[1][k-1]
        if choc(P[0][k], P[1][k]):
            return 2
        if compris(P[0][k], rg, rb) and compris(P[1][k], zb, zh):
            return 1
        T[k] = k*h
    return 0

#Création de la grille de tests : on teste que pour la moitié droite, et on copie à gauche ( symetrie du champ )
r1, z1 = np.arange(0, 6.1, 1), np.arange(-6, 6.1, 1)
r1, z1 = np.meshgrid(r1, z1)

def liste_points_cap():
    r_cap = []
    z_cap = []
    r_choc = []
    z_choc = []
    r_nope = []
    z_nope = []

    for i in range(len(r1)):
        for j in range(len(r1[0])):
            a = trouve_capture(0.1, np.pi/3, (r1[i][j], z1[i][j]), t_app, int(int(t_app) * 1.5)) 
            if a == 1:
                r_cap.append(r1[i][j])
                z_cap.append(z1[i][j])
            if a == 2:
                r_choc.append(r1[i][j])
                z_choc.append(z1[i][j])
            if a == 0:
                r_nope.append(r1[i][j])
                z_nope.append(z1[i][j])

    return r_cap, z_cap, r_choc, z_choc, r_nope, z_nope

def replicate(list_r, list_z):
    for i in range(1, len(list_r)):
        list_r.append(-list_r[i])
        list_z.append(list_z[i])
    return list_r, list_z

#print(r1, '\n', z1)

r_cap, z_cap, r_choc, z_choc, r_nope, z_nope = liste_points_cap()
r_cap1, z_cap1 = replicate(r_cap, z_cap)
r_choc1, z_choc1 = replicate(r_choc, z_choc)
r_nope1, z_nope1 = replicate(r_nope, z_nope)

N_points = 2 * len(r1) * len(r1[0]) - len(r1)

print("La proba que le débris soit capturé est de :", len(r_cap1)/N_points)
print("La proba que le débris entre en collision avec les parois est de :", len(r_choc1)/N_points)
print('La proba que le débris ne soit pas capturé est de :', len(r_nope1)/N_points)

plt.figure()

#Crée la forme du solenoide
plt.vlines(x = [-1, 1], ymin = [-1.5, -1.5], ymax = [1.5, 1.5], colors = 'teal')
plt.hlines(y = 1.5, xmin = -1, xmax = 1, colors = 'teal')
plt.hlines(y = -1.5, xmin = -1, xmax = 1, colors = 'teal')


for i in range(len(r_cap1)):
    if i == 0:
        plt.plot(r_cap1[0], z_cap1[0], color = 'red', label = 'Capturés', marker = '+', markersize = 12)
    else:
        plt.plot(r_cap1[i], z_cap1[i], color = 'red', marker = '+', markersize = 12)
for i in range(len(r_choc1)):
    if i == 0:
        plt.plot(r_choc1[0], z_choc1[0], color = 'green', label = 'Chocs', marker = '+', markersize = 12)
    else:
        plt.plot(r_choc1[i], z_choc1[i], color = 'green', marker = '+', markersize = 12)
for i in range(len(r_nope1)):
    if i == 0:
        plt.plot(r_nope1[0], z_nope1[0], color = 'blue', label = 'Non capturés', marker = '+', markersize = 12)
    else:
        plt.plot(r_nope1[i], z_nope1[i], color = 'blue', marker = '+', markersize = 12)

plt.title(label = 'Portée effective du dispositif', fontsize = '20' )
plt.xlabel('r (m)', fontsize = '20')
plt.ylabel('z (m)', fontsize = '20')

plt.xlim([-11, 11])
plt.ylim([-7, 7])
plt.xticks(fontsize='20')
plt.yticks(fontsize='20')
plt.legend()
plt.show()
