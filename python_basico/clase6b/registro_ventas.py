# REGISTRO DE VENTAS:
# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
# de tus productos. Cada producto tiene un nombre y una cantidad
# vendida. Implementa un programa en Python que utilice un diccionario
# para almacenar la información de las ventas. El programa debe permitir
# registrar las ventas de productos, actualizar la cantidad vendida de un
# producto existente y calcular el total de ventas diarias.
# (Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
# producto)

# Diccionario de ventas
ventas = {}

# Registrar ventas
ventas['Producto 1'] = int(input('Introduzca el numero de ventas del producto 1: '))
ventas['Producto 2'] = int(input('Introduzca el numero de ventas del producto 2: '))
ventas['Producto 3'] = int(input('Introduzca el numero de ventas del producto 3: '))

# Sumar el numero de ventas
ventas_total = sum(ventas.values())

print('El numero total de ventas es de ', ventas_total)

# Preguntar si desea actualizar el numero de ventas registradas


print('¿Desea actualizar el numero de ventas de cada producto? (Y/N): ') 
actualizacion = input('Si desea cambiar un producto en especifico, colocar el nombre del producto en clave: ')


if actualizacion.title() == 'Y':
    ventas['Producto 1'] = int(input('Introduzca el numero de ventas del producto 1: '))
    ventas['Producto 2'] = int(input('Introduzca el numero de ventas del producto 2: '))
    ventas['Producto 3'] = int(input('Introduzca el numero de ventas del producto 3: '))
    ventas_total = sum(ventas.values())
    print('El numero total de ventas es de ', ventas_total)
elif actualizacion.title() == 'N':
    print('Numero de ventas es de ', ventas_total)
elif actualizacion.title() == 'producto 1' or 'producto 2' or 'producto 3':
    if actualizacion.title() == 'Producto 1':
        ventas['Producto 1'] = int(input('Introduzca el numero de ventas del producto 1: '))
        ventas_total = sum(ventas.values())
        print('Numero de ventas es de ', ventas_total)
    elif actualizacion.title() =='Producto 2':
        ventas['Producto 2'] = int(input('Introduzca el numero de ventas del producto 2: '))
        ventas_total = sum(ventas.values())
        print('Numero de ventas es de ', ventas_total)
    elif actualizacion.title() == 'Producto 3':
        ventas['Producto 2'] = int(input('Introduzca el numero de ventas del producto 3: '))
        ventas_total = sum(ventas.values())
        print('Numero de ventas es de ', ventas_total)
    