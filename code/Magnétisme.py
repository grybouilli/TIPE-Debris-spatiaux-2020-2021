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
    def __init__ (self,r,theta,z):
        self.r = r
        self.theta = theta
        self.z = z

    def get_r(self):
        return(self.r)
    def get_theta(self):
        return(self.theta)
    def get_z(self):
        return(self.z)

    def set_r(self,r1):
        self.r = r1
    def set_theta(self,theta1):
        self.theta = theta1
    def set_z(self,z1):
        self.z = z1

