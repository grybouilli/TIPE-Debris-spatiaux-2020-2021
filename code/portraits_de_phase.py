import mouvement as mvt
import matplotlib.pyplot as plt
import numpy as np
import champ_mag as mag
import operateurs_vectoriels as opvec


figr = plt.figure()
figz = plt.figure()
axr = figr.gca()
axz = figz.gca()

# #Coords de depart :
# rd, zd = 1.5,3
# pos_r, pos_z, vit_r, vit_z = np.zeros(nverlet),np.zeros(nverlet),np.zeros(nverlet),np.zeros(nverlet)

# pos_r, pos_z, vit_r, vit_z = pos_vit_verlet(0.1, 0.1, (rd, zd), temps_verlet, nverlet) 
# axr.plot(pos_r[0], vit_r[0], color = 'red', marker = '+', markersize = 12)
# axz.plot(pos_z[0], vit_z[0], color = 'red', marker = '+', markersize = 12)

# portrait_r = axr.plot(pos_r, vit_r,color='r')[0]
# portrait_z = axz.plot(pos_z, vit_z,color='r')[0]

# add_arrow(portrait_r,size=30)
# add_arrow(portrait_z, size=30)


#plusieurs positions de départ:

colors = ['r','g','b','y']

axr.plot(mvt.pos_r[0], mvt.vit_r[0], color = colors[1], marker = '+', markersize = 12)
axz.plot(mvt.pos_z[0], mvt.vit_z[0], color = colors[1], marker = '+', markersize = 12)

portrait_r = axr.plot(mvt.pos_r, mvt.vit_r,color=colors[1])[0]
portrait_z = axz.plot(mvt.pos_r, mvt.vit_z,color=colors[1])[0]

opvec.add_arrow(portrait_r,size=30)
opvec.add_arrow(portrait_z, size=30)

axr.set_xlabel('r (m)',fontsize='40')
axr.set_ylabel('vitesse radiale (m.s^-1)',fontsize='40')

axz.set_xlabel('z (m)',fontsize='40')
axz.set_ylabel('vitesse selon z (m.s^-1)',fontsize='40')

plt.xticks(fontsize='40')
plt.yticks(fontsize='40')
plt.show()