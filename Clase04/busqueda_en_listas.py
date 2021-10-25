# -*- coding: utf-8 -*-
"""
@author: qagustina
"""

#%% 4.3: Búsquedas de un elemento (item1)
# funcion que recibe una lista y un elemento y devuelve la posición de la  
# última aparición de ese elemento en la lista (o -1 si el elemento no 
#                                                pertenece a la lista). 

def buscar_u_elemento(lista, e):
    pos = -1 
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            pass
    return pos

#%%  4.3: Búsquedas de un elemento  (item2)
# funcion que recibe una lista y un elemento y devuelve la cantidad de veces 
# que aparece el elemento en la lista. 
          
def buscar_n_elemento(lista, e):
    contador = 0
    #pos = -1
    for i, z in enumerate(lista):
        if z == e:
            contador += 1
            #pos = i
        #else:
            #pos = -1
    return contador

# si no encuentra devuelve 0
'''
buscar_n_elemento([8, 8, 9, 2, 18, 9, 8, 8, 9, 6], 8)
Out[74]: 4

buscar_n_elemento([8, 8, 9, 2, 18, 9, 8, 8, 9, 2, 2, 13, 12], 2)
Out[75]: 3

buscar_n_elemento([11, 8, 9, 2, 18, 11, 8, 11, 11, 2, 2, 13, 11], 11)
Out[76]: 5
'''
#%% 4.4: Búsqueda de máximo y mínimo
'''Devuelve el máximo de una lista, 
la lista debe ser no vacía y de números positivos.
'''
# m guarda el máximo de los elementos a medida que recorro la lista. 
# numeros positivos n > 0
# len(lista) > 0

def maximo(lista):
    
    while (len(lista) > 0): #no vacia
        m = 0 # Lo inicializo en 0
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e > m:
                m = e
        return m

#%%
def busqueda_lineal_lordenada(lista,e):
    lista.sort() # ordeno la lista
    pos = -1 
    for i, z in enumerate(lista):
        if z == e:   
            pos = i  
        elif z > e:
            break
    return pos