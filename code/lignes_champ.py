import champ_mag as mg
import numpy as np
import matplotlib.pyplot as plt

h = 0.2 #pas du maillage

w = mg.w
U = mg.U
V = mg.V

def point_suivant(rc, zc, h):
    br = mg.Br(rc, zc)
    bz = mg.Bz(rc, zc)
    norme = np.sqrt(br**2 + bz**2)
    dir_r = br/norme
    dir_z = bz/norme
    
    rs = rc + dir_r*h
    zs = zc + dir_z*h
    return rs, zs

def ligne_champ(r0, z0, h):
    rc, zc = r0, z0
    rs, zs = point_suivant(rc, zc, h)
    R, Z = [r0], [z0]
    k = 0
    
    while ((abs(r0-rs) >= h) or (abs(z0-zs) >= h)) and k<5000:
#        print(rc, zc)  #pour avoir un oeil sur le déroulement
        R.append(rs)
        Z.append(zs)
        rc, zc = rs, zs
        rs, zs = point_suivant(rc, zc, h)
        k += 1
    
    R1 = np.array(R)
    Z1 = np.array(Z)
    return R1, Z1


r, z = mg.r, mg.z

R1, Z1 = ligne_champ(0.9, 0, h)
plt.plot(R1, Z1, color = "r")
plt.plot(-R1, Z1, color = "r")
plt.plot(np.zeros(2 * len(r)), np.arange(-2*w, 2*w, h), color = "r")