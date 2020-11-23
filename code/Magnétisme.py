import numpy as np
import matplotlib.pyplot as plt
import random
#Rayon du solénoïde (m):
a = 5
#Intensité du courant dans les filaments (A):
i = 0
#Longueur du solénoïde (m):
L = 0
#Nombre de tour par mètre (tours.m*(-1)):
n = 0
#Perméabilité du vide (m.kg.s**(-2).A**(-2)):
mu0 = 1.25663706 * 10**(-6)

print(mu0)

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
    

