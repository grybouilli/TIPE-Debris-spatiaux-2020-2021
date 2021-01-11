import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.special import ellipk
from utilities import *
#Rayon du solénoïde (m):
a = 0.05
#Intensité du courant dans les filaments (A):
i = 5
#Longueur du solénoïde (m):
L = 1
#Nombre de tour par mètre (tours.m*(-1)):
n = 1000
#Perméabilité du vide (m.kg.s**(-2).A**(-2)):
mu0 = 1.25663706 * 10**(-6)



#Pour r qui se rapproche de 0:
# Calcule la composante du champ magnétique selon r à un instant donné
def Br(vec):

    pol = polar_of_cart(vec)
    r = pol.get_x()
    a = mu0 * n * i / 4
    xip = pol.get_z() + L/2
    xim = pol.get_z() - L/2

    def f(xi):
        return a*a*r/((xi*xi + a*a)**(3/2))
    
    return a * (f(xip) - f(xim))

# Calcule la composante du champ magnétique selon z à un instant donné
def Bz(vec):

    pol = polar_of_cart(vec)
    a = mu0 * n * i / 2
    xip = pol.get_z() + L/2
    xim = pol.get_z() - L/2

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
