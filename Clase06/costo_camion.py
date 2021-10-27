# 6.12
import informe_funciones


def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0
    for registro in camion:
        costo_total += registro['cajones']*registro['precio']
    return costo_total


# version anterior
# def costo_camion(archivo):
#     costo = 0.0
    
#     with open (archivo, 'rt') as archivo:
#         # n_row es la posicion, row es lo que hay en esa posicion
#         # start es opcional 
#         rows = csv.reader(archivo)
#         headers = next(rows)

#         for n_row, row in enumerate(rows, start=1):
#             # zip toma múltiples secuencias y las combina en un iterador.
#             # dict convierte en diccionario, en este caso los pares clave-valor
#             record = dict(zip(headers, row))  
#             try:
#                 ncajones = int(record['cajones'])
#                 precio = float(record['precio'])
#                 costo += ncajones * precio
#             except ValueError:
#                 print(f'Fila: {n_row}: No pude interpretar: {row}')
    
#     # print(f'Costo total:  ${costo:0.2f}.')
#     return costo

# import costo_camion
# costo_camion.costo_camion('../Data/camion.csv')
# output 
# >> 47671.15
