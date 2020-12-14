import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def afficher(x,y,name):
    plt.figure(name)
    plt.plot(x,y)
    plt.show()

def afficher_plusieurs(x,ys,names):
    plt.figure("graphe")
    for y in range(len(ys)):
        plt.plot(x, ys[y], label=names[y])
    plt.legend()
    plt.show()

