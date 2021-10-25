# Ejercicios de errores en el código
'''
@author : qagustina
'''
#%%

# Ejercicio 3.1 Función tiene_a()
# Comentario: El error es de Semántica
#    Lo corregí cambiando linea 12, expresion[i] == 'a' por if 'a' in expresion:
#    tambien agrege el contador de i dentro del if 
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion) 
    i = 0  
    while i<n:
        if 'a' in expresion:  
        #if expresion[i] == 'a':
            i += 1
            return True
        else:
            return False
        #i += 1


print(tiene_a('UNSAM 2020')) # False porque A mayuscula
print(tiene_a('abracadabra')) # True
print(tiene_a('La novela 1984 de George Orwell')) #True


#%%
# Ejercicio 3.2. Función tiene_a()
# Comentario: El error era de Sintaxis y estaba ubicado varias lineas.
#    Lo corregí agregando: 
#                          ':' faltantes en condiciones.
#                           condicion Else 
#                           Falso por False, y su identación.
#                           Tambien modifique identacion de incremento de i += 1 
#                           cambie = por == (uno es asignacion, y otro es evaluacion)        
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            i += 1
            return True
        else:
            return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

# %%
# Ejercicio 3.3. Función tiene_uno()
# Comentario: El error era de Tipo y estaba ubicado en la ultima linea.
# Mensaje de error: TypeError: object of type 'int' has no len(), es decir 
# el tipo de objeto entero no tiene funcion len() 
# Lo corregi cambiando tiene_uno(1984) por tiene_uno('1984')
# A continuación va el código corregido


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))


# %%
# Ejercicio 3.4: suma(a,b)
# Comentario: el error se daba en tiempo de ejecucion
# La variable c nunca era accedida, y lo solucioné agregando en la funcion return c
# A continuación va el codigo corregido

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# %%
# Ejercicio 3.5: Pisando memoria
# Comentario: El output de esta funcion, no da el resultado que esperamos. 
# Esto se daba porque se estaba pisando memoria, es decir despues del for todas las lineas
# eran iguales. 
# Lo corregi cambiando de linea registro={} colocándolo dentro del for.
# A continuación va el codigo corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={} # defino un diccionario en cada loop
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
# %%
