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

def xip(z):
    return z + mg.L/2

def xim(z):
    return z - mg.L/2

def tBr(z, r):
    xiplus = xip(z)
    ximo = xim(z)
    A = mg.mu0 * mg.n * mg.i / np.pi
    B = np.sqrt(mg.a / r)
    def func(r, xi):
        prem = (2 - petit_k(r, xi**2))/(2*petit_k(r, xi)) * defi.approx_K(petit_k(r, xi))
        dez = defi.approx_E(petit_k(r, xi))/petit_k(r, xi)
        return prem - dez
    return A * B * (func(r, xiplus) - func(r, ximo))

