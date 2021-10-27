# -*- coding: utf-8 -*-
"""
@author: qagustina
"""
# Ejercicio 6.6: Parsear un archivo CSV
import csv


def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando 
    el parámetro select, que debe ser una lista de nombres de las columnas
    a considerar.
    '''
    with open(nombre_archivo, encoding='utf-8') as f:
        filas = csv.reader(f)
        # Ejercicio 6.9: Trabajando sin encabezados
        if has_headers:

            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Ejercicio 6.9
            if has_headers:
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Ejercicio 6.8: Conversión de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
            else:
                # fila = tuple(lista)
                registro = (fila[0], fila[1])
            
            registros.append(registro)

    return registros

# Ejercicio 6.7: Selector de Columnas
# agrego argumento opcional en la funcion 
# lee todos los datos
camion = parse_csv('../Data/camion.csv')

# lee solo algunos datos 
cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])

# test
# precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
# precios