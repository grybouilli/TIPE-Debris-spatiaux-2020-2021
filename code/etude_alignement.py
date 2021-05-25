import champ_mag as mag
import aimantation as aim
import matplotlib.pyplot as plt
import numpy as np

m = 10
h = 5
l = 5
L = 5
# prends les variables de l'espace temps, la norme du moment magnétique, le moment d'inertie et l'angle initial
def angle_moment_petit(r,z,t,p,J_theta,alpha0):
    bz = mag.Bz(r,z)
    br = mag.Br(r,z)
    pulsation = np.sqrt(p*abs(bz) / J_theta)

    return (alpha0 - br/bz) * np.cos(pulsation * t) + br/bz 



def alpha_reel(r, z, p, J_theta, alpha0, tf, n):
    if tf == 0:
        return ([alpha0], [0])
    bz = mag.Bz(r, z)
    br = mag.Br(r, z)
    cste = p/J_theta
    
    h = tf/n #le pas d'int�gration
    Y = np.zeros(n)
    A = np.zeros(n)
    A[0] = alpha0
    T = np.zeros(n)
    
    for k in range (1, n):
        ak1 = cste*((br*np.cos(A[k-1])) - (bz*np.sin(A[k-1])))
        A[k] = A[k-1] + h*Y[k-1] + ((h**2)/2)*ak1
        
        ak = cste*((br*np.cos(A[k])) - (bz*np.sin(A[k])))
        Y[k] = Y[k-1] + (h/2)*(ak1 + ak)
        
        T[k] = T[k-1] + h
    
    return (A, T)


def alpha(r, z, p, J_theta, alpha0, t):
    return alpha_reel(r, z, p, J_theta, alpha0, t, int(t*200))[0][-1]

r = 10
z = 1
n_al = 0.181/(10**30)
N = n_al * h * l * L
moment_p = aim.norme_M_pop(r,z,N)
J = m*(h**2+l**2+L**2) / 12

#alpha approch� aux petits angles
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


#alpha r�el

alpha0 = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]
angle = []
temps = 0

for al0 in alpha0:
    al, T = alpha_reel(r, z, moment_p, J, al0, 20000000000000, 10000)
    angle.append(al)
    temps = T

plt.figure()
plt.plot(temps, angle[0], label = 'alpha0 = 0')
plt.plot(temps, angle[1], label = 'alpha0 = pi/6')
plt.plot(temps, angle[2], label = 'alpha0 = pi/4')
plt.plot(temps, angle[3], label = 'alpha0 = pi/3')
plt.plot(temps, angle[4], label = 'alpha0 = pi/2')

plt.xlabel('temps (s)')
plt.ylabel('alpha (rad)')
plt.legend()
plt.show()
