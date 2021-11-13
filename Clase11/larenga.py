# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:29:56 2021

@author: qagustina
"""

def pascal(n,k):
    '''
    Funcion recursiva que recibe parametros n (filas) y k (columnas).
    Devuelve el valor en la posicion pasada como parámetro.
    '''
    if n == k:
        res = 1
    elif k == 0:
        res = 1
    else:
        # evaluo fila anterior  misma col y fila anterior col anterior 
        res = pascal(n-1,k) + pascal(n-1, k-1)
    return res