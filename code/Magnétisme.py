import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.special import ellipk
from scipy.special import ellipe
from scipy.special import ellipkinc
from scipy.special import ellipeinc
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

#cas général 

def Br(r,z):
    c = (mu0 * n * i)/ np.pi 
    xip = z+L/2
    xim = z-L/2
    k_pos = (4*a*r)/((xip)**2 + (a+r)**2)
    k_neg = (4*a*r)/((xim)**2 + (a+r)**2)

    return c * np.sqrt(a/r) * (((2-k_pos) * K_int(np.sqrt(k_pos))/(2*np.sqrt(k_pos)) -  E_int(np.sqrt(k_pos)) / np.sqrt(k_pos) ) - ( (2-k_neg) * K_int(np.sqrt(k_neg))/(2*np.sqrt(k_neg)) -  E_int(np.sqrt(k_neg)) / np.sqrt(k_neg))) 
    
def Bz(r,z):
    c1 = (mu0 * n * i)/4
    xip = z+L/2
    xim = z-L/2
    phi = lambda xi, r : np.arctan(np.abs(xi/(a-r)))
    k_pos = (4*a*r)/((xip)**2 + (a+r)**2)
    k_neg = (4*a*r)/((xim)**2 + (a+r)**2)
    return( c1 * (
    (xip*np.sqrt(k_pos))/(np.pi*np.sqrt(a*r)) * K_int(np.sqrt(k_pos)) - (xim*np.sqrt(k_neg))/(np.pi*np.sqrt(a*r)) * K_int(np.sqrt(k_neg))
    +
    ((a-r)*xip / np.abs((a-r)*xip)) * Heuman(phi, k_pos) - ((a-r)*xim / np.abs((a-r)*xim)) * Heuman(phi, k_neg)))


# Dans le cas général 
#en utilisant scypi

#Complete ellipitc integral, first kind : K(k) = K(pi/2, k)
def K_int(k):
    K= np.zeros(len(k))
    for i in range(len(K)):
        K[i] = ellipk([K[i]])
    return K

#Complete ellipitc integral, second kind : E(k) = E(pi/2, k)
def E_int(k):
    E = np.zeros(len(k))
    for i in range(len(E)):
        E[i] = ellipe([E[i]])
    return E

def K_int2(phi, k):
    K= np.zeros(len(k))
    for i in range(len(K)):
        K[i] = ellipkinc([phi],[K[i]])
    return K


#Complete ellipitc integral, second kind : E(k) = E(pi/2, k)
def E_int2(phi, k):
    E = np.zeros(len(k))
    for i in range(len(E)):
        E[i] = ellipeinc([phi],[E[i]])
    return E

def Z_int(phi, k):
    return E_int2(phi,k) - (K_int2(phi,k) * E_int(k)) / K_int(k)

def Heuman(phi, k):
    return K_int2(phi, 1-k)/K_int(1-k) + 2/np.pi * K_int(k)*Z_int(phi, 1-k)

