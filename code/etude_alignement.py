import Magnétisme as mg
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np

m = 10
h = 5
l = 5
L = 5
# prends les variables de l'espace temps, la norme du moment magnétique, le moment d'inertie et l'angle initial
def angle_moment_petit(r,z,t,p,J_theta,alpha0):
    bz = mg.Bz(r,z)
    br = mg.Br(r,z)
    pulsation = np.sqrt(p*abs(bz) / J_theta)

    alpha_thau = np.arccos(1/(alpha0*(bz/br) - 1))
    return (alpha0 - br/bz) * np.cos(pulsation * t) + br/bz 



def alpha_reel(r, z, p, J_theta, alpha0, tf, n):
    bz = mg.Bz(r, z)
    br = mg.Br(r, z)
    cste = p/J_theta
    
    h = tf/n #le pas d'int�gration
    Y = np.zeros(n)
    A = np.zeros(n)
    A[0] = alpha0
    T = np.zeros(n)
    
    for k in range (1, n):
        Y[k] = Y[k-1] + h*cste*((br*np.cos(A[k-1])) - (bz*np.sin(A[k-1])))
        A[k] = A[k-1] + h*Y[k-1]
        T[k] = T[k-1] + h
    
    return (A, T)




r = 10
z = 1
moment_p = aim.norme_M(r,z)
J = m*(h**2+l**2+L**2) / 12


'''
t = np.linspace(0,50, 10000)
alpha_0 = [np.pi/3, np.pi/4, np.pi/6]
alpha = []

for a in alpha_0:
    al=angle_moment_petit(r,z,t,moment_p,J,a)
    alpha.append(al)
plt.figure()
plt.plot(t,alpha[0], label='alpha_0 = pi/3')
plt.plot(t,alpha[1], label='alpha_0 = pi/4')
plt.plot(t,alpha[2], label='alpha_0 = pi/6')

plt.xlabel('time (s)')
plt.ylabel('alpha (rad)')
plt.legend()
plt.show()
'''

alpha0 = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]
alpha = []
temps = 0

for al0 in alpha0:
    al, T = alpha_reel(r, z, moment_p, J, al0, 50, 10000)
    alpha.append(al)
    temps = T

plt.figure()
plt.plot(temps, alpha[0], label = 'alpha0 = 0')
plt.plot(temps, alpha[1], label = 'alpha0 = pi/6')
plt.plot(temps, alpha[2], label = 'alpha0 = pi/4')
plt.plot(temps, alpha[3], label = 'alpha0 = pi/3')
plt.plot(temps, alpha[4], label = 'alpha0 = pi/2')

plt.xlabel('temps (s)')
plt.ylabel('alpha (rad)')
plt.legend()
plt.show()