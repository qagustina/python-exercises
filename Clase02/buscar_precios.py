# 2.7: Buscar precios
f = open('../Data/precios.csv', 'rt', encoding='utf8')


def buscar_precio(fruta):
    for line in f:
        row = line.split(',')
        row_aux = row 
        if fruta in row_aux:
            print('El precio de un cajon de', fruta,'es:', row_aux[1])
            return row_aux[1] # return me permite cerrar el ciclo si la fruta esta en la lista.
    else:
        print(f'{fruta} no figura en el listado de precios.')
    f.close()


buscar_precio('Frambuesa')
buscar_precio('Caqui')
