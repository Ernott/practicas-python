palabra = str(input("Ingrese una palabra: "))
# Creamos un bucle que recorra el rango de letras introducido por el usuario y las imprima de forma deletreada empezando por la ultima letra
for i in range(len(palabra)):
    print(palabra[-i-1])