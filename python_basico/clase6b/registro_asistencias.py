# REGISTRO DE ASISTENCIAS:
# Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
# estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
# una lista de fechas en las que asistió a clases. Implementa un programa
# en Python que utilice un diccionario para almacenar la información de las
# asistencias. El programa debe permitir registrar la asistencia de los
# estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
# estudiantes y las fechas en las que asistieron.
# (Pista: puedes comenzar con un diccionario vacío y construir un
# diccionario de listas)

asistencias = dict()

# registrar asistencias de los estudiantes
asistencias['Estudiante1'] = ['2022-01-01', '2022-01-03', '2022-01-05']
asistencias['Estudiante2'] = ['2022-01-02', '2022-01-05', '2022-01-07']
asistencias['Estudiante3'] = ['2022-01-01', '2022-01-05', '2022-01-07']
print(asistencias)