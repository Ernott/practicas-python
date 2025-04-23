# Descripcion: este programa solicita  al usuario un numero y crea un bucle que recorre el rango 
# ascendente y descendente del carácter '*'
num = int(input("Introduce un número: "))
# Creamos un bucle que recorra el rango de números introducido por el usuario
for i in range(num):
    # Creamos una variable que contenga el caracter '*' multiplicado por el número del rango
    caracter1 = '*' * (i+1)
    print(caracter1)
# Creamos un bucle que recorra el rango de números introducido por el usuario
for i in range(num-1):
    # Creamos una variable que contenga el caracter '*' multiplicado por el número del rango
    caracter2 = '*' * (num-i-1)
    print(caracter2)