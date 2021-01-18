from Magnétisme import *
from utilities import *
import librairies.display as disp
import matplotlib.pyplot as plt
import numpy as np


def K_int(k):
    (n,m) = len(k), len(k[0])
    K= np.zeros(len(k))
    for i in range(n):
        for j in  range(m):
            K[i] = ellipk([k[i][j]])
    return K

def E_int(k):
    (n,m) = len(k), len(k[0])
    E = np.zeros(len(k))
    for i in range(n):
        for j in range(m):
            E[i] = ellipe([k[i][j]])
    return E

def K_int2(phi, k):
    (n,m) = len(k), len(k[0])
    K= np.zeros(len(k))
    for i in range(n):
        for j in range(m):
            K[i] = ellipkinc([phi[i][j]],[k[i][j]])
    return K

#Complete ellipitc integral, second kind : E(k) = E(pi/2, k)
def E_int2(phi, k):
    (n,m) = len(k), len(k[0])
    E = np.zeros(len(k))
    for i in range(n):
        for j in range(m):
            E[i] = ellipeinc([phi[i][j]],[k[i][j]])
    return E
