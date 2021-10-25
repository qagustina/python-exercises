# %% Ejercicio 3.17: Tablas de multiplicar
'''
@author : qagustina
'''
# Comentario: Función linea_sep()
# 5 los primeros cinco espacios
# 3*9 = 27 porque 3 espacios (entre los numeros de 0 a 9)
# 10 por cada raya (-) por numero de 0 a 9
def linea_sep():
    print(f'-' * (5+(3*9)+10)) 


numeros = range(10) 
print('   ', end='')
for i in numeros:
    print(f'{i:>3d}', end= ' ')  
print()
linea_sep()


for i in numeros:
    print(f'{i}:', end=' ')
    for j in numeros:
        print(f'{i*j:>3}', end=' ') 
    print()

print()
# si recibe como parametro N, me permite hacer una tabla del tamaño 
# que le pase por parametro, lo que hace que el codigo no este 
# hardcodeado a un rango de 10, como esta actualmente la funcion.
# %%
