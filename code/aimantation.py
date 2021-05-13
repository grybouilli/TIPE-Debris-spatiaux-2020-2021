import Magnétisme as mg
import numpy as np

#Définitions des constantes

H_BARRE = 1.054 * 10**(-34) #J.S
m_e = 9.11 * 10**(-31) #kg
n_NBTI = 1.25 * 10**29 #électrons/m^3


def E_Fermi(n):
    a = (3 * np.pi*np.pi * n) ** (2/3)
    return H_BARRE**2 * a / (2 * m_e)

EF_NBTI = E_Fermi(n_NBTI) #J


