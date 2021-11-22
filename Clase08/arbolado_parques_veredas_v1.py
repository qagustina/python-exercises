# -*- coding: utf-8 -*-
"""
@author: qagustina
"""
# 8.9: Comparando especies en parques y en veredas
import os
import pandas as pd

directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'

def abrir_y_leer_archivos():
    fname_p = os.path.join(directorio, archivo_parques) # abro 
    fname_v = os.path.join(directorio, archivo_veredas)
    df_parques = pd.read_csv(fname_p) # leo csv parques 
    df_veredas = pd.read_csv(fname_v) # leo csv veredas
    return df_parques, df_veredas


df_parques, df_veredas = abrir_y_leer_archivos()

especie_p = 'Tipuana Tipu'
especie_v = 'Tipuana tipu'

columna_p = 'nombre_cie'
columna_v = 'nombre_cientifico'


def parques():
    # Parques
    df_tipas_parques = df_parques[df_parques[columna_p] == especie_p]
    # Columnas con las que me interesa trabajar
    cols_p = ['altura_tot', 'diametro'] 
    df_tipas_parques = df_tipas_parques[cols_p]
    # Copia del dataframe asi no modifico el original
    df_tipas_parques = df_parques[df_parques[columna_p] == especie_p][cols_p].copy()
    # RENAME
    df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura_arbol", "diametro": "diametro_altura_pecho"})
    # AGREGO COLUMNA
    df_tipas_parques['ambiente']='parque'
    return df_tipas_parques


def veredas():
    # Veredas
    df_tipas_veredas = df_veredas[df_veredas[columna_v] == especie_v]
    cols_v = ['altura_arbol', 'diametro_altura_pecho']
    df_tipas_veredas = df_tipas_veredas[cols_v]
    # COPIA
    df_tipas_veredas = df_veredas[df_veredas[columna_v] == especie_v][cols_v].copy()
    # AGREGO COLUMNA
    df_tipas_veredas['ambiente']='vereda'
    return df_tipas_veredas


df_tipas_parques = parques()
df_tipas_veredas = veredas()


def concatenar_df():
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    return df_tipas


df_tipas = concatenar_df()


def graficar():
    # boxplot para los diámetros a la altura del pecho de las tipas distinguiendo los ambientes
    df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente', figsize=(12,9))
    # boxplot para altura de las tipas distinguiendo los ambientes
    df_tipas.boxplot('altura_arbol',by = 'ambiente', figsize=(12,9))
    
graficar()