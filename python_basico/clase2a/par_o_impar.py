# ----- Creamos un script que solicite un número y una potencia al usuario, para luego verifique si el resultado es par o impar -----
# Pedimos el número al usuario
numero = int(input('Ingrese un número: '))
# Pedimos la potencia al usuario
potencia = int(input('Ingrese la potencia: '))
# Calculamos el resultado de elevar el número a la potencia ingresada
resultado = numero ** potencia
# Verificamos SI(if) el resultado es
if resultado % 2 == 0:
    print('El resultado', resultado, 'es par')
else:
    print('El resultado', resultado, 'es impar')