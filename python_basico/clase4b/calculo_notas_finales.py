# Importamos la biblioteca de numpy
import numpy as np
# Creamos el array de la puntuacion
array_puntuacion=np.array([
    [2,3,1,9],
    [5,1,10,10],
    [8,9,9,10]
])
# Identificamos las variables de puntuacion dentro del array
examen1=array_puntuacion[:,0]
examen2=array_puntuacion[:,1]
examen3=array_puntuacion[:,2]
participacion=array_puntuacion[:,3]
# Modificamos las puntuaciones para dar la nota final
notafinal = (examen1 * 0.3) + (examen2 * 0.3) + (examen3 * 0.3) + (participacion * 0.1)
# Damos la nota de cada estudiante
for i in range(len(notafinal)):
    print('La nota final del estudiante', i+1, 'es', notafinal[i])