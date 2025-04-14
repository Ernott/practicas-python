# Crea un array con 15 números enteros aleatorios entre 1 y 100
import numpy as np
r_array = np.random.randint(1, 101, 15)
print(r_array)
print('----------------------------------------')
# Multiplica todos los elementos del array usando un bucle y después usando un método de numpy. Compara los resultados
multi = 1
for i in r_array:
    multi *= i
print('Resultado usando un bucle:', multi)

multi_numpy = np.prod(r_array)
print('Resultado usando un método de numpy:', multi_numpy)
print('----------------------------------------')
# Crea otro array con 15 números decimales aleatorios entre 0 y 1
fl_array = np.random.rand(15)
print(fl_array)
print('----------------------------------------')
# Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
# operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)
suma_operador = r_array + fl_array
print('Suma usando un operador:', suma_operador)

suma_numpy = np.add(r_array, fl_array)
print('Suma usando una función de numpy:', suma_numpy)
print('----------------------------------------')
# Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
resta_operador = r_array - fl_array
print('Resta usando un operador:', resta_operador)

resta_numpy = np.subtract(r_array, fl_array)
print('Resta usando una función de numpy:', resta_numpy)
print('----------------------------------------')
# Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y después con una función de numpy
multi_operador = r_array * fl_array
print('Multiplicación usando un operador:', multi_operador)

multi_numpy = np.multiply(r_array, fl_array)
print('Multiplicación usando una función de numpy:', multi_numpy)
print('----------------------------------------')
# Encuentra el valor más alto del primer array que has creado.
print(max(r_array))
print('----------------------------------------')
# Calcula la media (mean), la mediana (median) y al deviación estandar (standard
# deviation) de los arrays (Nota: No nos importa el significado matemático de estos
# valores, lo importante es que encuentres que función de numpy necesitas.
print(np.mean(r_array))
print(np.median(r_array))
print(np.std(r_array))