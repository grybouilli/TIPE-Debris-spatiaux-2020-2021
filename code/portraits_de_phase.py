import mouvement as mvt
import matplotlib.pyplot as plt
import numpy as np
import champ_mag as mag
import operateurs_vectoriels as opvec

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

def pos_vit_verlet(m, alpha0, p0, tf, n):
    h = tf/n
    V = np.zeros((n, n))
    P = np.zeros((n, n))
    P[0][0], P[1][0] = p0
    T = np.zeros(n)
    
    for k in range (1, n) :
        a_r_n, a_z_n = mvt.ac(m, P[0][k-1], P[1][k-1], T[k-1], alpha0)
        
        P[0][k] = P[0][k-1] + h*V[0][k-1] + ((h**2)/2)*a_r_n
        P[1][k] = P[1][k-1] + h*V[1][k-1] + ((h**2)/2)*a_z_n
        
        T[k] = T[k-1] + h
        
        a_r_n1, a_z_n1 = mvt.ac(m, P[0][k], P[1][k], T[k], alpha0)
        V[0][k] = V[0][k-1] + (h/2)*(a_r_n + a_r_n1)
        V[1][k] = V[1][k-1] + (h/2)*(a_z_n + a_z_n1)
        
    return (P[0], P[1], V[0], V[1])



figr = plt.figure()
figz = plt.figure()
axr = figr.gca()
axz = figz.gca()

# #Coords de depart :
# rd, zd = 1.5,3
nverlet = 500
temps_verlet = 240
# pos_r, pos_z, vit_r, vit_z = np.zeros(nverlet),np.zeros(nverlet),np.zeros(nverlet),np.zeros(nverlet)

# pos_r, pos_z, vit_r, vit_z = pos_vit_verlet(0.1, 0.1, (rd, zd), temps_verlet, nverlet) 
# axr.plot(pos_r[0], vit_r[0], color = 'red', marker = '+', markersize = 12)
# axz.plot(pos_z[0], vit_z[0], color = 'red', marker = '+', markersize = 12)

# portrait_r = axr.plot(pos_r, vit_r,color='r')[0]
# portrait_z = axz.plot(pos_z, vit_z,color='r')[0]

# add_arrow(portrait_r,size=30)
# add_arrow(portrait_z, size=30)


#plusieurs positions de départ:

RD,ZD= np.arange(0,2.,0.5) , np.array([2.5,2.5,3,3])
colors = ['r','g','b','y']
nportrait = len(RD)
pos_r_m,pos_z_m,vit_r_m,vit_z_m = np.zeros((nportrait,nverlet)),np.zeros((nportrait,nverlet)),np.zeros((nportrait,nverlet)),np.zeros((nportrait,nverlet))
for i in range (nportrait):
    pos_r_m[i],pos_z_m[i],vit_r_m[i],vit_z_m[i] = pos_vit_verlet(0.1,0.1,(RD[i],ZD[i]),temps_verlet,nverlet)
    axr.plot(pos_r_m[i][0], vit_r_m[i][0], color = colors[i], marker = '+', markersize = 12)
    axz.plot(pos_z_m[i][0], vit_z_m[i][0], color = colors[i], marker = '+', markersize = 12)

    portrait_r = axr.plot(pos_r_m[i], vit_r_m[i],color=colors[i])[0]
    portrait_z = axz.plot(pos_z_m[i], vit_z_m[i],color=colors[i])[0]

    add_arrow(portrait_r,size=30)
    add_arrow(portrait_z, size=30)

plt.show()