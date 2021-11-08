# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:30:30 2021

@author: qagustina
"""
# 10.2: Iteración sobre objetos
# 10.14: Expresiones generadoras como argumentos en funciones.

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes
     
        
    def __iter__(self):
       '''hace iterable a la Clase camion'''
       return self.lotes.__iter__()


    def precio_total(self):
        # comprension de listas para el precio total
        # return sum([l.costo() for l in self.lotes])
        return sum(l.costo() for l in self.lotes) # expr. generadora
    
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    
    def __contains__(self, nombre):
        '''any(): True si al menos un elemento de un iterable es verdadero
        False si todos los elementos son falsos o si un iterable está vacío'''
        # compresion de listas
        # return any([lote.nombre == nombre for lote in self.lotes])
        # expr. generadora
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __len__(self):
        '''método especial len '''
        return self.lotes.__len__()
    
    
    def __getitem__(self,a):
        return self.lotes.__getitem__(a)
    
    
    def __repr__(self):
        '''genera una salida mas agradable los elementos que hay en camion'''
        return f'Camion({self.lotes})'
    
    
    def __str__(self):
        '''devuelve una representacion como cadena de camion y sus lotes.'''
        print(f'Camion con {len(self.lotes)} lotes:')
        s = []
        for l in self.lotes:
            s.append(f'Lote de {l.cajones} de {l.nombre}, pagados a ${l.precio} cada uno.')
        return '\n'.join(s)
        

# import informe_final
# camion = informe_final.leer_camion('../Data/camion.csv')
# camion
# print(camion)