# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:30:40 2021

@author: qagustina
"""
# 8.1: Segundos vividos
from datetime import datetime


def vida_en_segundos(fecha_nac):
    '''
    Toma como entrada una cadena fecha_nac en formato: 'dd/mm/AAAA'
    Devuelve un float: segundos_vividos
    '''
    fecha_nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    fecha_actual = datetime.now()
    cantidad_vivida = fecha_actual - fecha_nac 
    segundos_vividos = cantidad_vivida.total_seconds()
    
    return segundos_vividos


fecha_nac = '21/11/1996'
segundos_vividos = vida_en_segundos(fecha_nac)
print(segundos_vividos)


# testeo con fecha cercana para comprobar que me den los segundos correctos
# fecha_nac = '31/10/2021'


    
    
    
    
    



