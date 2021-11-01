# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 15:50:13 2021

@author: qagustina
"""
# Ejercicio 8.5: Recorrer el árbol de archivos
import os 


def archivos_png(directorio):
    # recorro todos los archivos de ese directorio separando en root 
    # (ruta de archivo incluyendo carpetas), dirs (carpetas), files (archivos).
    os.chdir(directorio) # me muevo al directorio que le paso como parametro
    for root, dirs, files in os.walk("."):
        [print(name) for name in files if name.endswith('.png')]
        
        
directorio = archivos_png('../Data/ordenar')