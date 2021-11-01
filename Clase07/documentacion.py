# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 00:03:13 2021

@author: qagustina
"""
# Ejercicio 7.10: Funciones y documentación

# Para cada una de las siguientes funciones: 
# * Pensá cuál es el contrato de la función. * 
# Agregale la documentación adecuada.
# * Comentá el código si te parece que aporta. * 
# Detectá si hay invariantes de ciclo y comentalo al final de la función

def valor_absoluto(n):
    '''
    Recibe un número y devuelve su valor absoluto
    '''
    if n >= 0:
        return n
    else:
        return -n
    

def suma_pares(l):
    '''
    Recibe una lista y si existen numeros pares devulve la suma de los mismos.
    Si no, devuelve 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res


def veces(a, b):
    '''
    Recibe dos números y realiza una multiplicacion rústica.
    Suma 'a', b veces.
    '''
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a 
        nb -= 1
    return res


def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2 
        else:
            n = 3 * n + 1
        res += 1
    return res
