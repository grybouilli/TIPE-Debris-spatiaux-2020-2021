import numpy as np
import matplotlib.pyplot as plt
import random
import math
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

class Vecteur:
    def __init__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return(self.x)
    def get_y(self):
        return(self.y)
    def get_z(self):
        return(self.z)

    def set_x(self,x1):
        self.x = x1
    def set_y(self,y1):
        self.y = y1
    def set_z(self,z1):
        self.z = z1

    def __add__(self, other):
        return Vecteur(self.x+other.get_x(), self.y+other.get_y(), self.z+other.get_z())
    
    def __str__(self):
        return "Vecteur avec x = %s, y = %s, z = %s" % (self.get_x(), self.get_y(), self.get_z())
    

def prod_scal(vect1,vect2):
    (x1,x2) = (vect1.get_x(),vect2.get_x())
    (y1,y2) = (vect1.get_y(),vect2.get_y())
    (z1,z2) = (vect1.get_z(),vect2.get_z())
    return x1*x2 + y1*y2 + z1*z2
    
def prod_vec(vec1, vec2):
    (x1,x2) = vec1.get_x(), vec2.get_x()
    (y1,y2) = vec1.get_y(), vec2.get_y()
    (z1,z2) = vec1.get_z(), vec2.get_z()

    return Vecteur(y1*z2-y2*z1, z1*x2-x1*z2, y2*x1-y1*x2)
    
def polar_of_cart(vec):
    r = np.sqrt(vec.get_x()**2 + vec.get_y()**2)
    if r == 0:
        return Vecteur(0,0,0)
    return Vecteur(r, np.arccos( vec.get_x() / r ),vec.get_z())

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

#Calcule la composante du champ magnétique selon z à un instant donné
def Bz(vec):

    pol = polar_of_cart(vec)
    a = mu0 * n * i / 2
    xip = pol.get_z() + L/2
    xim = pol.get_z() - L/2

    def f(xi):
        return xi / np.sqrt(xi*xi + a*a)
    
    return a * (f(xip) - f(xim))

test = Vecteur(2, 0, 2)

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

print(K(2))