# ----- Escribimos un programa que divida dos números enteros ingresados por el usuario -----
# Pedimos el dividendo al usuario
dividendo = int(input('Ingrese el dividendo: '))
# Pedimos el divisor al usuario
divisor = int(input('Ingrese el divisor: '))
# Verificamos SI(if) el divisor es diferente de cero
if divisor != 0:
    # Calculamos el resultado de la división
    resultado = dividendo / divisor
    # Imprimimos el resultado
    print('El resultado de la división es:', resultado)
# En caso contrario(NO) imprimimos un mensaje de división por cero
else:
    print('No es posible dividir por cero')