# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:17:02 2021

@author: qagustina
"""
# 9.1: Objetos como estructura de datos
# 9.2: Agregá algunos métodos 
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        # otra manera: 
        # self.costo = self.cajones * self.precio # se crea atributo costo
        return self.cajones * self.precio
        
    def vender(self, n):
        # n es la cantidad de cajones a vender
        self.cajones -= n
    # 9.9
    def __repr__(self):
        '''
        Genera una salida mas agradable
        '''
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
        

# 9.3 Herencia
class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
    # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor

    def costo(self):
        return self.factor * super().costo()
   
    def rematar(self):
        self.vender(self.cajones)