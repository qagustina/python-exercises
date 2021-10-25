'''
@author : qagustina
'''
# Ejercicio 3.18: Lectura de los árboles de un parque
# Lista de diccionarios
import csv
from pprint import pprint


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

print('\n')
print('Lista de Especies:')
print('\n')
pprint(especies(lista_arboles))

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


print('\n')
print('Las cinco especies más frecuentes en Parque GENERAL PAZ')
pprint(contar_ejemplares(lista_arboles))
print('\n')

