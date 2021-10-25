# -*- coding: utf-8 -*-
"""
@author: qagustina
"""

def invertir_lista(lista):
    invertida = []
    for e in lista:
          invertida = [e] + invertida
    return invertida

# invertir_lista([1, 2, 3, 4, 5])
# Out[20]: [5, 4, 3, 2, 1]

# invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# Out[21]: ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']