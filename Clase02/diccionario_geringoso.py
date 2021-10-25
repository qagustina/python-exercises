# 2.14: Diccionario geringoso.
cadena = 'todos somos programadores'


def geringoso(cadena):
    cadena_aux = ''
    for c in cadena:
        if c in 'aeiou':
            cadena_aux = cadena_aux + c +'p'+ c
        else:
            cadena_aux = cadena_aux + c
    return cadena_aux

#cadena_aux = geringoso(cadena)
#print(cadena_aux)

frase = 'banana manzana mandarina'
lista = frase.split() # lista de palabras


def diccionario_geringoso(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = geringoso(palabra)
    return diccionario


diccionario = diccionario_geringoso(lista)
print(diccionario)