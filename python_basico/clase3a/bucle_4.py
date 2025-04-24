# Descripcion: Este programa solicita al usuario una frase y una letra, y luego cuenta cuantas veces 
# aparece la letra en la frase.
frase = str(input("Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))
# Creamos un bucle que valide que la letra introducida sea una letra
while letra.isalpha() == False or len(letra) > 1:
    # Si la letra no es una letra, se le pide al usuario que introduzca una letra
    print("Lo que ha introducido no es una letra, por favor introduzca una letra")
    # Se le pide al usuario que introduzca una letra
    letra = str(input("Ingrese una letra: "))
# Creamos un contador que cuente cuantas veces aparece la letra en la frase
contador = 0
# Creamos un bucle que recorra el rango de letras de la frase introducida por el usuario
for i in range(len(frase)):
    if frase[i] == letra:
        contador = contador + 1
print('La letra ',letra,' aparece ',contador,' veces en la frase ',frase)