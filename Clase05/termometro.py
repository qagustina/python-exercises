# -*- coding: utf-8 -*-

# Ejercicio 5.6: Gaussiana
import random 
import numpy as np


def medir_temp(n):
    mediciones = [random.normalvariate(37.5, 0.2) for t in range(n)]
    # Ejercicio 5.8: Guardar temperaturas
    temperaturas = np.array([mediciones])
    np.save('../Data/temperaturas', temperaturas)
    return mediciones


def resumen_temp(n):
    mediciones = medir_temp(n)
    
    maximo = max(mediciones)
    minimo = min(mediciones)
    media = sum(mediciones) / n
    # mediana
    mediciones.sort() # primero ordeno la lista
    longitud = len(mediciones)
    mitad = int(longitud / 2)
    
    if longitud%2 == 0:
        # si es par calculo la mediana
        mediana = (mediciones[mitad - 1] + mediciones[mitad]) / 2
    else:
        # si es impar es el elemento central
        mediana = mediciones[mitad]

    # print(f'mediciones: {mediciones}')
    # print(f'maximo: {maximo:.5f}, minimo: {minimo:.5f}, promedio: {media:.5f}, mediana: {mediana:.5f}')
    return (maximo, minimo, media, mediana)

