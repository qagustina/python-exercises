# Ejercicio 1.5
altura = 100    
rebote = (0.6) * 100 


cantidad_rebotes = 1 


while cantidad_rebotes <= 10:
    print(cantidad_rebotes, rebote)
    cantidad_rebotes = cantidad_rebotes + 1
    rebote = round(rebote * 0.6, ndigits=4)


# output 
"""
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
"""

