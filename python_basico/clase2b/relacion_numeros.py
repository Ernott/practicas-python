# ----- Hacemos un programa que pida al usuario 3 números y muestre por pantalla si la suma de los dos primeros es igual al tercero -----#
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese un número: "))
# Se evalua si la suma de los dos primeros números es igual al tercero
if num3 == num1 + num2:
    print(f"El número {num3} es la suma de {num1} y {num2}")
elif num2 == num1 + num3:
    print(f"El número {num2} es la suma de {num1} y {num3}")
elif num1 == num2 + num3:
    print(f"El número {num1} es la suma de {num2} y {num3}")