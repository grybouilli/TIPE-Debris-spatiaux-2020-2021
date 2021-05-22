import scipy.integrate as sc
import numpy as np
import matplotlib.pyplot as plt

#Rayon du solénoïde (m):
a = 1
#Intensité du courant dans les filaments (A):
i = 1000000
#Longueur du solénoïde (m):
L = 3
#Nombre de tour par mètre (tours.m*(-1)) (on peut avoir un diamètre de fil de 0.3mm):
n = 3000
#Perméabilité du vide (T.m/A)
mu0 = 12.566370614 * 10**(-7)


def int_Br(theta, r, z):
    xip = z + L/2
    xim = z - L/2
    
    cp = xip**2 + r**2 + a**2 - 2*a*r*np.cos(theta)
    cm = xim**2 + r**2 + a**2 - 2*a*r*np.cos(theta)
    
    intp = np.cos(theta)/(np.sqrt(cp))
    intm = np.cos(theta)/(np.sqrt(cm))
    
    return (intp - intm)


def int_Bz(theta, r, z):
    xip = z + L/2
    xim = z - L/2
    
    cp = xip**2 + r**2 + a**2 - 2*a*r*np.cos(theta)
    cm = xim**2 + r**2 + a**2 - 2*a*r*np.cos(theta)
    
    c = r**2 + a**2 - 2*a*r*np.cos(theta)
    dp = c*np.sqrt(cp)
    dm = c*np.sqrt(cm)
    
    npos = xip*(a - r*np.cos(theta))
    nm = xim*(a - r*np.cos(theta))
    
    intp = npos/dp
    intm = nm/dm
    
    return (intp - intm)


def Br(r, z):
    cste = -(a*mu0*n*i)/(2*np.pi)
    inte = lambda theta : int_Br(theta, r, z)
    return cste*sc.quad(inte, 0, np.pi)[0]

def Bz(r, z):
    cste = (a*mu0*n*i)/(2*np.pi)
    inte = lambda theta : int_Bz(theta, r, z)
    return cste*sc.quad(inte, 0, np.pi)[0]

def norme_B(r, z):
    return np.sqrt((Br(r, z)**2) + (Bz(r, z)**2))

w = 11/10 * L

fig, ax = plt.subplots()


r, z = np.arange(-w, w, 0.2), np.arange(-w, w, 0.2)
r, z = np.meshgrid(r, z)
z += 0.5 #pour mieux centrer la figure
U, V = np.zeros((len(r), len(r))), np.zeros((len(z), len(z)))

for i in range(len(r)):
    for j in range (len(r)):
        U[i][j] = Br(r[i][j], z[i][j])
        V[i][j] = Bz(r[i][j], z[i][j])

'''
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

mo = len(U)
moo = len(V)
print("La norme au milieu du champ est",norme_B(0, 0),"normalement",  mu0 * n * i)


ax.quiver(r, z, U, V, color = "grey")
ax.set_title('Vecteur champ magnétique')

plt.show()
    
''' 