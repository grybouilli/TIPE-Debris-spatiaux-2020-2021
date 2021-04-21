import Magnétisme as mg
import numpy as np

def petit_k(r,xi):
    return np.sqrt((4*mg.a*r) / (xi**2 (mg.a+r)**2))

