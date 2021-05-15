import numpy as np
from numpy.core.defchararray import upper

#NB: Aucun des vecteurs que l'on manipule ne dépend de theta donc les dérivées selon theta sont forcément nulles. On adapte le code en les écrivant nulle part

'''
derivée partielle de la fonction u selon r, où :
- u est une fonction à deux variables de l'espace cylindrique
-derive_r renvoie une fonction prenant deux arguments, r et z les coordonnées de l'espace cylindrique, où r est nécessairement un tableau
'''
def derive_r(u):
    def u_prime_r(r,z):
        n = len(r)
        up = np.zeros(n)
        for i in range(n-1):
            up[i] = (u(r[i+1], z) - u(r[i],z)) / (r[i+1]-r[i]) 
        return up
    return u_prime_r

'''
derivée partielle de la fonction u selon z, où :
- u est une fonction à deux variables de l'espace cylindrique
-derive_z renvoie une fonction prenant deux arguments, r et z les coordonnées de l'espace cylindrique, où z est nécessairement un tableau
'''
def derive_z(u):
    def u_prime_z(r,z):
        n = len(z)
        up = np.zeros(n)
        for i in range(n-1):
            up[i] = (u(r, z[i+1]) - u(r,z[i])) / (z[i+1]-z[i]) 
        return up
    return u_prime_z

def gradient_cyl(u):
    return derive_r(u),derive_z(u)

'''
Soit u = u_r e_r + u_z e_z un vecteur en coordonnées cylindriques, rotationnel renvoie le rotationnel de u qui sera alors selon e_theta
'''
def rotationnel(u_r,u_z):
    return derive_z(u_r) - derive_r(u_z)

