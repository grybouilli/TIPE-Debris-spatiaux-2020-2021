import Magnétisme as mg
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np

m = 10
h = 5
l = 5
L = 5
# prends les variables de l'espace temps, la norme du moment magnétique, le moment d'inertie et l'angle initial
def angle_alpha_moment(r,z,t,p,J_theta,alpha0):
    bz = mg.Bz(r,z)
    br = mg.Br(r,z)
    pulsation = np.sqrt(p*abs(bz) / J_theta)

    alpha_thau = np.arccos(1/(alpha0*(bz/br) - 1))
    return (alpha0 - br/bz) * np.cos(pulsation * t) + br/bz , alpha_thau/pulsation

'''
r = 100
z = 1
moment_p = aim.norme_M(r,z)
J = m*(h**2+l**2+L**2) / 12

t = np.linspace(0,1000, 10000)
alpha_0 = [np.pi/3, np.pi/4, np.pi/6]
alpha = []
thau = []

for a in alpha_0:
    al,th =angle_alpha_moment(r,z,t,moment_p,J,a)
    alpha.append(al)
    thau.append(th)
plt.figure()
plt.plot(t,alpha[0], label='alpha_0 = pi/3')
plt.plot(t,alpha[1], label='alpha_0 = pi/4')
plt.plot(t,alpha[2], label='alpha_0 = pi/6')

alpha_0_max = max(alpha_0)
for t in thau:
    plt.vlines(t, - alpha_0_max, alpha_0_max)

plt.xlabel('time (s)')
plt.ylabel('alpha (rad)')
plt.legend()
plt.show()
'''