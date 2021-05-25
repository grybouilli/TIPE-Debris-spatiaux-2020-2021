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
    
    while ((abs(r0-rs) >= h) or (abs(z0-zs) >= h)) and k<149:
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
R1, Z1 = R1[:18], Z1[:18]
R4, Z4 = ligne_champ(0.7, 0, h)
R4, Z4 = R4[:36], Z4[:36]
R2, Z2 = ligne_champ(0.5, 0, h)
R2, Z2 = R2[:69], Z2[:69]
R3, Z3 = ligne_champ(0.2, 0, h)
R3, Z3 = R3[:70], Z3[:70]
sol = (np.arange(-mg.a, mg.a + mg.a/10, (2*mg.a / 20)), np.arange(-mg.L/2, mg.L/2 + (mg.L/30), (mg.L/30)))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

plt.plot(Z1, R1, color = "r")
plt.plot(-Z1, R1, color = "r")
plt.plot(Z1, -R1, color = "r")
plt.plot(-Z1, -R1, color = "r")

plt.plot(Z4, R4, color = "r")
plt.plot(-Z4, R4, color = "r")
plt.plot(Z4, -R4, color = "r")
plt.plot(-Z4, -R4, color = "r")

plt.plot(Z2, R2, color = "r")
plt.plot(-Z2, R2, color = "r")
plt.plot(Z2, -R2, color = "r")
plt.plot(-Z2, -R2, color = "r")

plt.plot(Z3, R3, color = "r")
plt.plot(-Z3, R3, color = "r")
plt.plot(Z3, -R3, color = "r")
plt.plot(-Z3, -R3, color = "r")

plt.plot(np.arange(-2*w, 2*w, h), np.zeros(2 * len(r)), color = "r")

plt.plot((np.zeros(len(sol[0])) + mg.L/2), sol[0], color = "b")
plt.plot((np.zeros(len(sol[0])) - mg.L/2), sol[0], color = "b")
plt.plot(sol[1], (np.zeros(len(sol[1])) + mg.a), color = "b")
plt.plot(sol[1], (np.zeros(len(sol[1])) - mg.a), color = "b")