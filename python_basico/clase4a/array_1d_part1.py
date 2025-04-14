# Crea un array_1 lleno de ceros con una longitud de 8 elementos
import numpy as np
array_1 = np.zeros(8, dtype = np.int8)
print(array_1)
print("-----------------------------")
# Haz que todos los elementos de este array sean igual a 2
array_1[:] = 2
print(array_1)
print("-----------------------------")
# Crea un array_2 que contenga todos los numeros pares del 1 al 10
array_2 = np.arange(2,11,2)
print(array_2)
print("-----------------------------")
# Revierte el array_2 y guardalo en una variable independiente
array_2_revertido = np.zeros(5)
array_2_revertido[:] = array_2[::-1]
print('Array revertido es: ', array_2_revertido)
print('Array original es: ', array_2)
print("-----------------------------")
# Suma todos los elementos del array_2 usando un bucle y despues usando un metodo de numpy. Compara los resultados
suma = 0
for i in array_2:
    suma += i
print('metodo del bucle es ', suma)
print('metodo numpy es ', np.sum(array_2))
print("-----------------------------")
# Revierte array_2 y guárdalo en una variable independiente
array_3 = np.flip(array_2)
print(array_3)
# Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y array_3
comun_1_2 = np.intersect1d (array_1,array_2)
comun_2_3 = np.intersect1d (array_2, array_3)
print('Los elementos comunes del array 1 y array 2 son ', comun_1_2)
print('Los elementos comunes del array 2 y array 3 son ', comun_2_3)
# Crea un arrays lleno de 1 con una longitud dada por el usuario
lon = int(input('Coloque la longitud de 1: '))
array_4 = np.ones(lon, dtype=np.int8)
print(array_4)