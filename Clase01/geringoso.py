# Ejercicio 1.18
cadena = input('ingresa alguna palabra para convertirla en geringoso:')
cadena_aux = '' # definimos una nueva cadena (vacia) para ir armando la nueva cadena con la 'p' incluida segun vocal

for c in cadena:
    if c in 'aeiou':
        cadena_aux = cadena_aux + c +'p'+ c
    else:
        cadena_aux = cadena_aux + c

print(cadena_aux)
