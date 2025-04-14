# ADMINISTRACION DE PROYECTOS:
# Eres un gerente de proyectos y necesitas un programa para administrar
# las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
# una descripción y un responsable asignado. Implementa un programa en
# Python que utilice un diccionario para almacenar la información de las
# tareas. El programa debe permitir agregar nuevas tareas, asignar
# responsables a las tareas existentes, actualizar las descripciones de las
# tareas y mostrar la lista completa de tareas y responsables.
# (Pista: puedes comenzar con un diccionario vacío y construir un
# diccionario de diccionarios)

tareas = {}
bucle = True

while bucle:
    tarea_nombre = input('Introduzca el nombre de la tarea (Escriba done para finalizar): ')
    if tarea_nombre.lower() == 'done':
        bucle = False
    else:
        descripcion = input('Introduzca la descripción de la tarea: ')
        responsable = input('Introduzca el responsable de la tarea: ')
        tareas[tarea_nombre] = {'descripcion': descripcion, 'responsable': responsable}

print('Lista de tareas:')
for nombre, detalles in tareas.items():
    print('Tarea:', nombre)
    print('Descripcion:', detalles['descripcion'])
    print('Responsable:', detalles['responsable'])
    print()