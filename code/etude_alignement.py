import Magnétisme as mg
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np

m = 10
h = 5
l = 5
L = 5
def angle_alpha_moment(t,r,z,p,J_theta,alpha0):
    bz = mg.Bz(r,z)
    br = mg.Br(r,z)
    pulsation = np.sqrt(p*bz) / J_theta
    return (alpha0 - br/bz) * np.cos(pulsation * t) + br/bz

r = 100
z = 0
moment_p = aim.norme_M(r,z)
J = m*(h**2+l**2+L**2) / 12

t = np.linspace(0,5, 1000)
alpha = angle_alpha_moment(t,r,z,moment_p,J, 0)

plt.figure()
plt.plot(t,alpha)
plt.show()
