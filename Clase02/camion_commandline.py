# 2.10: Ejecución desde la línea de comandos con parámetros
import csv
import sys


def costo_camion(archivo):

    with open(archivo, 'rt', encoding='utf8') as archivo:

        rows = csv.reader(archivo)
        headers = next(rows)
        costo = 0.0

        for row in rows:
            try:
                cajones = float(row[1])
                precio = float(row[2])
                costo += cajones * precio
            
            except ValueError:
                print(f'{archivo} Se encontraron datos faltantes para el cálculo del costo total.')
    

        #print(f'Costo total:  ${costo:0.2f}.')
        return costo

if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = '../Data/camion.csv'


costo = costo_camion(archivo)
print(f'Costo total:  ${costo:0.2f}.')
