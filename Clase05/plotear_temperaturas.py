# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:01:31 2021

@author: qagustina
"""
# Ejercicio 5.9
import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas, bins=20)
    plt.xlabel("temperatura (grados)")
    plt.ylabel("error gaussiano (grados)")
    plt.title("Temperaturas Simuladas")
    plt.show()

plotear_temperaturas()
