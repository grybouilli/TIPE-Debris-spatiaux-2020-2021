import numpy as np
from numpy.core.defchararray import upper

#NB: Aucun des vecteurs que l'on manipule ne dépend de theta donc les dérivées selon theta sont forcément nulles. On adapte le code en les écrivant nulle part

'''
derivée partielle de la fonction u selon r, où :
- u est une fonction à deux variables de l'espace cylindrique
-derive_r renvoie une fonction prenant deux arguments, r et z les coordonnées de l'espace cylindrique
'''
def derive_r(u, eps):
    def u_prime_r(r,z):
        return (u(r+eps,z)-u(r-eps,z)) / (eps) 
    return u_prime_r

'''
derivée partielle de la fonction u selon z, où :
- u est une fonction à deux variables de l'espace cylindrique
-derive_z renvoie une fonction prenant deux arguments, r et z les coordonnées de l'espace cylindrique
'''
def derive_z(u, eps):
    def u_prime_z(r,z):
        return (u(r,z+eps)-u(r,z-eps)) / (eps) 
    return u_prime_z

def gradient_cyl(u):
    return derive_r(u),derive_z(u)

'''
Soit u = u_r e_r + u_z e_z un vecteur en coordonnées cylindriques, rotationnel renvoie le rotationnel de u qui sera alors selon e_theta
'''
def rotationnel(u_r,u_z):
    return derive_z(u_r) - derive_r(u_z)

def norme(u_r,u_z):
    return np.sqrt(u_r**2 + u_z**2)

def add_arrow(line, position=None, direction='right', size=15, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle='-|>', color=color),
        size=size
    )