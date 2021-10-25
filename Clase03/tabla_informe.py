# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:21:10 2021

@author: aagus
"""
# informe.py
import csv

# 2.16: Lista de diccionarios
# Modificado : Ejercicio 3.9: La función zip()
def leer_camion(archivo):
    '''
   Lee un archivo de lotes en un camión 
   y lo devuelve como lista de diccionarios con claves
   nombre, cajones, precio.

   '''
    precios_camion = []
    
    with open(archivo, 'rt') as archivo:
        
        filas = csv.reader(archivo)
        encabezados = next(filas)
        for fila in filas:
            registro = dict(zip(encabezados, fila))
            try:
                registro['cajones'] = int(registro['cajones'])
                registro['precio'] = float(registro['precio'])
                precios_camion.append(registro)
            except ValueError:
                print('Se encontraron datos faltantes para la operación.')
                
    return precios_camion


precios_camion = leer_camion('../Data/camion.csv')


# 2.17: Diccionarios como contenedores
# Uso Doc-strings para documentar adecuadamente.
def leer_precios(archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
   '''
    precios = {}  
    with open (archivo, 'rt', encoding='utf8') as archivo:
        
        rows = csv.reader(archivo)  
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print('Aviso: se encontraron datos faltantes para la operación.')
    
    return precios

precios = leer_precios('../Data/precios.csv')
# print(precios)


# Ejercicio 3.13: Recolectar datos
def hacer_informe(precios_camion, precios):
    lista = []
    for lote in precios_camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        total = (lote['nombre'], lote['cajones'], precio_venta, round(cambio, ndigits=4))
        lista.append(total)
    return lista

lista = hacer_informe(precios_camion, precios)

# Ejercicio 3.16: Un desafío de formato
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(precios_camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for nombre, cajones, precio, cambio in informe:
    precio = f'${precio}'
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    