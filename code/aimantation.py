import Magnétisme as mg
import numpy as np

#Définitions des constantes

#Constante de Planck réduite
H_BARRE = 1.054 * 10**(-34) #J.S

#Masse d'un électron
m_e = 9.11 * 10**(-31) #kg

#Densité en électron du Nb-Ti
n_NBTI = 1.25 * 10**29 #électrons/m^3

#Charge élémentaire
e = 1.602 * 10**(-19) #C

#Magnéton de Bohr
MU_B = e * H_BARRE / (2 * m_e) #J/T

def E_Fermi(n):
    a = (3 * np.pi*np.pi * n) ** (2/3)
    return H_BARRE**2 * a / (2 * m_e)

EF_NBTI = E_Fermi(n_NBTI) #J

def norme_M(r, z):
    B = mg.normeB(r, z)
    return 3 * MU_B**2 * n_NBTI * B / (2*EF_NBTI)

def vect_direct(r, z):
    a = mg.normeB(r, z)
    return (mg.Br(r, z)/ a, mg.Bz(r, z)/a)

def rotation(alpha, vect):
    a = np.cos(alpha)
    b = np.sin(alpha)
    (x, y) = vect
    xx = x*a - y*b
    yy = x*b + y*a
    return (xx, yy)