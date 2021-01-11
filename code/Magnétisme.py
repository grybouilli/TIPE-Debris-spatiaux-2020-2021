import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.special import ellipk
from scipy.special import ellipe
from utilities import *
#Rayon du solénoïde (m):
a = 2
#Intensité du courant dans les filaments (A):
i = 5
#Longueur du solénoïde (m):
L = 10
#Nombre de tour par mètre (tours.m*(-1)):
n = 100000
#Perméabilité du vide (m.kg.s**(-2).A**(-2)):
mu0 = 1.25663706 * 10**(-6)



#Pour r qui se rapproche de 0:
# Calcule la composante du champ magnétique selon r à un instant donné
def Br0(r, z):
    a = mu0 * n * i / 4
    xip = z + L/2
    xim = z - L/2

    def f(xi):
        return a*a*r/((xi*xi + a*a)**(3/2))
    
    return a * (f(xip) - f(xim))


# Calcule la composante du champ magnétique selon z à un instant donné
def Bz0(r, z):

    a = mu0 * n * i / 2
    xip = z + L/2
    xim = z - L/2

    def f(xi):
        return xi / np.sqrt(xi*xi + a*a)
    
    return a * (f(xip) - f(xim))



#Renvoie le vecteur champ magnétique à un instant donné
def calc_magn1(vec):
    return Vecteur(Br(vec), 0, Bz(vec))


# Dans le cas général 
#en utilisant scypi

#Complete ellipitc integral, first kind : K(k) = K(pi/2, k)
def K_int(k):
    return ellipk([k**2])


#Complete ellipitc integral, second kind : E(k) = E(pi/2, k)
def E_int(k):
    return ellipe([k**2])