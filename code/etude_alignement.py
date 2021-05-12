from Magnétisme import *
import matplotlib.pyplot as plt
import numpy as np

def angle_alpha_moment(t,r,z,p,J_theta,alpha0):
    bz = Bz(r,z)
    br = Br(r,z)
    pulsation = np.sqrt(p*Bz) / J_theta
    return (alpha0 - br/bz) * np.cos(pulsation * t) + br/bz
