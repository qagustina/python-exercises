#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ejercicio 7.7
import fileparse
from lote import Lote
import formato_tabla # 9.5
from camion import Camion


# Ejercicio 10.2: Iteración sobre objetos
def leer_camion(nombre_archivo):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios


# version ejercicio 9.4
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista

   
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))
    print(type(precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    # formateador = formato_tabla.FormatoTablaTXT()
    # formateador = formato_tabla.FormatoTablaCSV()
    formateador = formato_tabla.FormatoTablaHTML()
    imprimir_informe(data_informe, formateador)

    
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)