import csv
from pprint import pprint


# 2.15: Lista de tuplas
def leer_camion(archivo):
    registros = [] # inicializo lista vacia
    with open(archivo, 'rt') as archivo:
        rows = csv.reader(archivo)
        next(rows) # Saltear el encabezado
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2])) # tuplas
            registros.append(lote)
    return registros


camion = leer_camion('../Data/camion.csv')
print(camion)  


# 2.16: Lista de diccionarios
def leer_camion(archivo):
    with open(archivo, 'rt') as archivo:
        precios = []
        rows = csv.reader(archivo)
        next(archivo)
        for row in rows:
            lote = {
                'nombre': row[0],
                'cajones': int(row[1]),
                'precio': float(row[2])
            }
            precios.append(lote)
    return precios


camion_v1 = leer_camion('../Data/camion.csv')
pprint(camion_v1) 


# 2.17: Diccionarios como contenedores
# Uso Doc-strings para documentar adecuadamente.
def leer_precios(archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
   '''
    with open (archivo, 'rt', encoding='utf8') as archivo:
        rows = csv.reader(archivo)
        precios = {}  
        
        for row in rows:
            try:
                precios[row[0]] = row[1]
            except IndexError:
                print('Aviso: se encontraron datos faltantes para la operación.')
    
    return precios

precios = leer_precios('../Data/precios.csv')
print(precios)