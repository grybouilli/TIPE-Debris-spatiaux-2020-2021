import Magnétisme as mg
import numpy as np
import definitions_elliptiques as defi

def petit_k(r,xi):
    return np.sqrt((4*mg.a*r) / (xi**2 + (mg.a+r)**2))

def dk_dz(r, xi):
    A = np.sqrt(4*mg.a*r)
    return A * (-xi) * ( xi**2 + (mg.a + r)**2 )**(-3/2)

def dk_dr(r, xi):
    prem = mg.a / (np.sqrt((mg.a * r)**2 + xi**2 ) * np.sqrt(mg.a * r))
    deuz = 2*np.sqrt(mg.a * r) * (mg.a + r) / ( (mg.a + r)**2 + xi**2 )**(-3/2)
    return prem - deuz