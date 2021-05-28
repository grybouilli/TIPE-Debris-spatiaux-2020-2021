import mouvement as mv
import etude_alignement as ali
import numpy as np
import matplotlib.pyplot as plt

alpha0 = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]

#Coord de base :
rd, zd = 0.2, 3

r0, z0 = mv.pos_verlet(0.1, alpha0[0], (rd, zd), 250, 600)
r1, z1 = mv.pos_verlet(0.1, alpha0[1], (rd, zd), 250, 600)
r2, z2 = mv.pos_verlet(0.1, alpha0[2], (rd, zd), 250, 600)
r3, z3 = mv.pos_verlet(0.1, alpha0[3], (rd, zd), 250, 600)
r4, z4 = mv.pos_verlet(0.1, alpha0[4], (rd, zd), 250, 600)

plt.figure()
plt.plot(rd, zd, color = 'red', marker = '+', markersize = 12)

plt.plot(r0, z0, label = 'alpha0 = 0', linewidth = 2)
plt.plot(r1, z1, label = 'alpha0 = pi/6', linewidth = 2)
plt.plot(r2, z2, label = 'alpha0 = pi/4', linewidth = 2)
plt.plot(r3, z3, label = 'alpha0 = pi/3', linewidth = 2)
plt.plot(r4, z4, label = 'alpha0 = pi/2', linewidth = 2)

plt.vlines(x = [-1, 1], ymin = [-1.5, -1.5], ymax = [1.5, 1.5], colors = 'teal')
plt.hlines(y = 1.5, xmin = -1, xmax = 1, colors = 'teal')
plt.hlines(y = -1.5, xmin = -1, xmax = 1, colors = 'teal')

plt.xlabel('r (m)', fontsize = '20')
plt.ylabel('z (m)', fontsize = '20')

plt.xticks(fontsize = '20')
plt.yticks(fontsize = '20')
plt.legend(fontsize = '20')
plt.title('Essais avec différentes valeurs de alpha0')

plt.xlim([-5, 10])
plt.ylim([-5, 5])

plt.show()