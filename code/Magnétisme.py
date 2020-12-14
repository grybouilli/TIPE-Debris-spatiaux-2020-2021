import numpy as np
import matplotlib.pyplot as plt
import random
import math
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
def Br(r, z):
    a = mu0 * n * i / 4
    xip = z + L/2
    xim = z - L/2

    def f(xi):
        return a*a*r/((xi*xi + a*a)**(3/2))
    
    return a * (f(xip) - f(xim))


# Calcule la composante du champ magnétique selon z à un instant donné
def Bz(r, z):

    a = mu0 * n * i / 2
    xip = z + L/2
    xim = z - L/2

    def f(xi):
        return xi / np.sqrt(xi*xi + a*a)
    
    return a * (f(xip) - f(xim))


#Renvoie le vecteur champ magnétique à un instant donné
def calc_magn1(vec):
    return Vecteur(Br(vec), 0, Bz(vec))


# Dans le cas général (?)
"Complete ellipitc integral, second kind : E(k) = E(pi/2, k)"

def K(k):
    n = 1000
    a, b = 0, np.pi/4
    x = np.linspace(a, b, n)
    def f(theta):
        return 1 / np.sqrt( 1 - k * np.sin(theta) * np.sin(theta))
    y = f(x)
    res = 0
    for i in range(n-1):
        res += (x[i+1] - x[i])/(2*n) * (y[i] + y[i+1])
    return res * ()