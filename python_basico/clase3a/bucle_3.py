# Descripcion: Programa que solicita una palabra y la deletrea por la ultima letra de manera descendente
palabra = str(input("Ingrese una palabra: "))
# Creamos un bucle que recorra el rango de letras introducido por el usuario y las imprima
#  de forma deletreada empezando por la ultima letra
for i in range(len(palabra)):
    print(palabra[-i-1])