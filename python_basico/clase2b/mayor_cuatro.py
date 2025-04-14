#----- Mayor de cuatro números -----#
# Escribir un programa que pida al usuario 4 números y muestre por pantalla el mayor
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese un número: "))
num4 = int(input("Ingrese un número: "))
# Se evalua cual de los números es mayor
if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"El número mayor es: {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"El número mayor es: {num3}")
else:
    print(f"El número mayor es: {num4}")