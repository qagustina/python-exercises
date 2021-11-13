# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:56:26 2021

@author: qagustina
"""

# Ejercicio 11.14: precio_alquiler ~ superficie
import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


# Usando la función que definimos antes, ajustá los datos con una recta.
# Graficá los datos junto con la recta del ajuste.
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

n = 50
minx = 0
maxx = 500

# Ahora ajustamos con las fórmulas que vimos antes
a, b = ajuste_lineal_simple(superficie, alquiler)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Calculá el error cuadrático medio del ajuste que hiciste recién.
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())