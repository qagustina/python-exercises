'''
@author : qagustina
'''
# Ejercicio 3.18: Lectura de los árboles de un parque
# Lista de diccionarios
import csv
# from pprint import pprint


def leer_parque(archivo, parque):
    lista_arboles = []

    with open(archivo, 'rt', encoding='utf8') as archivo:
        rows = csv.reader(archivo)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row)) # combino el encabezado con cada fila
            if parque == record['espacio_ve']:
                lista_arboles.append(record)

    return lista_arboles


parque = "GENERAL PAZ"
lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
# pprint(lista_arboles) 


# 3.19: Determinar las especies en un parque
# A partir de una lista de diccionarios recibida como parámetro lista_arboles,
# se genera una lista con las especies y luego se aplica set a esa lista generada.

def especies(lista_arboles):
    especies = []
    for row in lista_arboles:
        especies.append(row['nombre_com'])
    especies = set(especies) 
    return especies

# print('\n')
# print('Lista de Especies:')
# print('\n')
# pprint(especies(lista_arboles))

# 3.20: Contar ejemplares por especie
# Funcion contar_ejemplares(lista_arboles) recibe una lista de diccionarios del ejercicio 3.18 
# se aplica funcion Counter y se llama al metodo most_common para listar las 5 especies mas frecuentes,
# y luego se convierte a diccionario la salida

from collections import Counter


def contar_ejemplares(lista_arboles):
    lista = [] # lista especies 
    
    for row in lista_arboles:
        lista.append(row['nombre_com'])
    
    contar_especies = Counter(lista).most_common(5)
    dicc_contado = dict(contar_especies)

    return dicc_contado


# print('\n')
# print('Las cinco especies más frecuentes en Parque GENERAL PAZ')
# pprint(contar_ejemplares(lista_arboles))
# print('\n')

# 4.15: Lectura de todos los árboles
# Lista de diccionarios por cada arbol 
def leer_arboles(archivo):
    '''
    documentar
    '''
    arboleda = []
    
    with open(archivo, 'rt', encoding='utf8') as archivo:
        
        rows = csv.reader(archivo)
        headers = next(rows)
        
        for row in rows:
            record = dict(zip(headers, row))
            arboleda.append(record)
            
    return arboleda


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
# pprint(arboleda)

# Ejercicio 4.16: Lista de altos de Jacarandá

# Comprension de Listas 

# Usando comprensión de listas y la variable arboleda armo una lista de 
# la altura de los árboles Jacaranda.
h=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(h)

# creo esta nueva de lista de diametros para poder plotear y=h(altura), x=d(diametro)
d = [float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(d)


# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
# Tuplas de alura y diametro de árboles de Jacarandá.
altura_diametro=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# print(altura_diametro)


import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 5.25: Histograma de altos de Jacarandás
def plot_alturas_jacarandas():
    plt.hist(h, bins=16)
    plt.title('Altos de Jacarandás')
    plt.show()


# Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
# convierto la lista de pares en un array
hd = np.array(altura_diametro)
# slicing
d = hd[:,1]
h = hd[:,0] 

def scatter_hd(hd):
    # 'x' and 'y' with size 3255.
    colors = np.random.rand(3255)
    plt.scatter(d, h, alpha=0.5, c=colors) 
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

plot_alturas_jacarandas()
scatter_hd(hd)