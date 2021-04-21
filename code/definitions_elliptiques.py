import numpy as np 
import math
import matplotlib.pyplot as plt 

k = 0.5
precision = 10**(-20)

#Prend le terme général d'une série;
#Calcule le premier terme inférieur à precision
def serie_stat(serie, epsilon, start, k):
    n = start
    while abs(serie(n, k)) >= epsilon:
        n += 1
    return n

#Pour ne pas calculer les fact 100 000 fois, on stocke assez de valeurs 
def fact(n):
    m = [1]
    for i in range(n):
        m.append(m[i]*(i+1))
    return m

facto = fact(80)

#T.g de E(k)
def suite_E(n, k):
    a = facto[2*n]
    b = 2**(2*n)
    c = facto[n]**2
    return (a/(b*c))**2 * k**(2*n)/(1-2*n)

#T.g de K(k)
def suite_K(n, k):
    a = facto[2*n]
    b = 2**(2*n)
    c = facto[n]**2
    return (a/(b*c))**2 * k**(2*n)
#Ou alors expressions des dérivées selon k sur Wikipédia...

#T.g de d(K)/dk
def suite_dKk(n, k):
    a = facto[2*n + 2]
    b = 2**(2*n + 2)
    c = facto[n + 1]**2
    return (2*n + 2) * (a/(b*c))**2 * k**(2*n + 1)

#T.g de d(E)/dk
def suite_dEk(n, k):
    a = facto[2*n + 2]
    b = 2**(2*n + 2)
    c = facto[n + 1]**2
    return (2*n + 2) * (a/(b*c))**2 * k**(2*n + 1)/(1-2*(n+1))

#T.g de E(k)/k
def suite_Esk(n, k):
    a = facto[2*n + 2]
    b = 2**(2*n + 2)
    c = facto[n + 1]**2
    return (a/(b*c))**2 * k**(2*n + 1)/(1-2*(n+1))

# T.g de d(E/k)/dk 
def suite_dEskk(n, k):
    a = facto[2*n + 4]
    b = 2**(2*n + 4)
    c = facto[n + 2]**2
    return (2*n + 3) * (a/(b*c))**2 * k**(2*n + 1)/(1-2*(n+1))

#Graphe de la suite/serie
def print_suite(suite, n, k):
    plt.figure()
    x = np.linspace(0, n, n+1)
    y = np.zeros(n+1)
    for i in range(n+1):
        y[i] = suite(i, k)
    plt.plot(x, y)
    plt.show()

#Calcule la série
def serie(suite, n, k):
    res = 0
    for i in range(n):
        res += suite(i, k)
    return res

#Indice au bout duquel les termes ajoutés à la somme sont inf à precision
N_K = serie_stat(suite_K, precision, 0, k)
N_E = serie_stat(suite_E, precision, 0, k)
N_dKk = serie_stat(suite_dKk, precision, 0, k)
N_dEk = serie_stat(suite_dEk, precision, 0, k)
N_Esk = serie_stat(suite_Esk, precision, 0, k)
N_dEskk = serie_stat(suite_dEskk, precision, 0, k)

print(N_K, N_E, N_dKk, N_dEk, N_Esk, N_dEskk)

#Calcul des fonctions à partir des approximations
def approx_E(k):
    return serie(suite_E, N_E, k)

def approx_K(k):
    return serie(suite_K, N_K, k)

def approx_dKk(k):
    return serie(suite_dKk, N_dKk, k)

def approx_dEk(k):
    return serie(suite_dEk, N_dEk, k)

def approx_Esk(k):
    return serie(suite_Esk, N_Esk, k)

def approx_dEskk(k):
    return serie(suite_dEskk, N_dEskk, k)