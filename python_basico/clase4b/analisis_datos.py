import numpy as np
# Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un 
# curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una 
# participación en clase. Quieres calcular la nota final de cada estudiante, donde los 
# exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase 
# vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, 
# donde n es el número de estudiantes. Cada columna representa una de las calificaciones 
# y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para 
# calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola 
# columna.

# Creamos un conjunto de calificaciones 

evaluacion = np.array([0.3,0.3,0.3,0.1])
estudiantes = int(input('numero de estudiantes: '))

# Creamos un bucle para guardar cuantos alumnos son en la clase

for estudiante in range(estudiantes):
    print(estudiante + 1)

# Una vez confirmado el numero de estudiantes el bucle termina

# Calculo e impresion de la evaluacion de estudiantes