# Descripcion: Programa solicita al usuario que coloque una clave preestablecida (1234), el bucle no
# para de mostar error hasta colocarla correctamente  
clave = input("Introduce la clave: ")
# Creamos un bucle que recorra el rango de números introducido por el usuario
while clave != "1234":
    print("Clave incorrecta")
    clave = input("Introduce la clave: ")
print("Clave correcta")