# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:51:10 2021

@author: qagustina
"""
# Ejercicio 6.6: Parsear un archivo CSV
# Ejercicio 7.6
import csv


def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando 
    el parámetro select, que debe ser una lista de nombres de las columnas
    a considerar.
    '''

    filas = csv.reader(lines)
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
    
    for n_fila, fila in enumerate(filas):
        # Ejercicio 7.2
        try:
            if not fila:    # Saltear filas vacías
                continue
            # Ejercicio 6.9
            if has_headers:
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Ejercicio 6.8: Conversión de tipo
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
        
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
            else:
                # fila = tuple(lista)
                registro = (fila[0], fila[1])
                    
            # Ejercicio 7.1
            if select and (has_headers==False):
                raise RuntimeError("Para seleccionar, necesito encabezados.")
            
            registros.append(registro)    
        # 7.2
        except ValueError as e:
            if not silence_errors:
                print(f'Fila: {n_fila}: No pude interpretar: {fila}')
                print(f'Fila: {n_fila} Motivo: ', e)
           
         # registros.append(registro)

    return registros

# Ejercicio 6.7
# agrego argumento opcional en la funcion 
# lee todos los datos
# camion = parse_csv('../Data/camion.csv')

# lee solo algunos datos 
# cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])


# Ejercicio: 6.9
# test1 = parse_csv('../Data/precios.csv', select=['nombre', 'precio'], has_headers=False)
# test2 = parse_csv('../Data/missing.csv', types=[str, int, float])
