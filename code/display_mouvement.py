import mouvement as mvt
import champ_mag as mag
import matplotlib.pyplot as plt
import numpy as np
import operateurs_vectoriels as op

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')

#Coords de depart :
xd, yd = 0.5 , 3

alpha_init = mag.Br(xd,yd)/mag.Bz(xd,yd)
print(alpha_init)
pos_r, pos_z, vit_r, vit_z = mvt.verlet_avec_collision(0.1, alpha_init, (xd, yd), 200, 600)
sol = (np.arange(-mag.a, mag.a + mag.a/10, (2*mag.a / 20)), np.arange(-mag.L/2, mag.L/2 + (mag.L/30), (mag.L/30)))

plt.plot(xd, yd, color = 'red', marker = '+', markersize = 12)
plt.plot((np.zeros(len(sol[1])) + mag.a), sol[1], color = "b")
plt.plot((np.zeros(len(sol[1])) - mag.a), sol[1], color = "b")
plt.plot(sol[0], (np.zeros(len(sol[0])) + mag.L/2), color = "b")
plt.plot(sol[0], (np.zeros(len(sol[0])) - mag.L/2), color = "b")

trajectoire = plt.plot(pos_r, pos_z, color = 'r', linewidth = 2)[0]

plt.xlabel('r (m)',fontsize='40')
plt.ylabel('z (m)',fontsize='40')
plt.xticks(fontsize='40')
plt.yticks(fontsize='40')

op.add_arrow(trajectoire,size=50)
plt.show()
