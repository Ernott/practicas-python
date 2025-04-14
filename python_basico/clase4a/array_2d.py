# Crea un arrays lleno de 1s con una longitud dada por el usuario
import numpy as np
lon = int(input('Coloque la longitud del array: '))
array_ones = np.ones(lon)
print(array_ones)
print('--------------------------')
# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
filas = int(input('Coloque el numero de filas: '))
columnas = int(input('coloque el numero de columnas: '))
if filas * columnas == lon:
    nuevo_array = np.reshape(array_ones, (filas,columnas))
    print('La nueva forma es:')
    print(nuevo_array)
else:
    print('ERROR numero de filas por columnas no es igual a la longitud del Array')
print('--------------------------')
# Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)
if filas * columnas == lon:
    matriz_identidad = np.eye(filas, columnas)
    print('La matriz de identidad es: ')
    print(matriz_identidad)
else:
    print('ERROR numero de filas por columnas no es igual a la longitud del Array')
print('--------------------------')
# Concatena ambas estructuras horizontalmente y verticalmente
# (Pista: Investiga el funcionamiento de concatenate() y de vstack() y de hstack() de numpy)

if filas * columnas == lon:
    array_concatenado = np.concatenate((nuevo_array, matriz_identidad), axis=0)
    print('Concatenados horizontalmente: ')
    print(array_concatenado)
    array_v = np.vstack((nuevo_array, matriz_identidad))
    print('Concatenados verticalmente: ')
    print(array_v)
    array_h = np.hstack((nuevo_array, matriz_identidad))
    print('Concatenados horizontalmente: ')
    print(array_h)
else:
    print('ERROR numero de filas por columnas no es igual a la longitud del Array')

print('--------------------------')