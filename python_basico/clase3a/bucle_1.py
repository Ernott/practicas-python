# Crea un programa que pida un número al usuario y escriba una pirámide de asteriscos con los números desde 1 hasta el número que ha introducido.
# Por ejemplo, si el usuario ha introducido el número 6 la pirámide será:
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
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