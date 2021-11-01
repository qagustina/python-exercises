# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:32:23 2021

@author: qagustina
"""
# Ejercicio 8.10
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

# COPIA
dh = df['12-25-2014':].copy()


delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 20.0 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot(figsize=(12,9))


# delta_t = -1 porque la onda tarda 1 hora en llegar a San Fernando.

# delta_h = 20.0 
# freq_horaria = 4 # 4 para 15min, 60 para 1min
# cant_horas = 24 
# deltah_h = cant_horas - freq_horaria