# Creamos la clave de acceso
clave = input("Introduce la clave: ")
# Creamos un bucle que recorra el rango de números introducido por el usuario
while clave != "1234":
    print("Clave incorrecta")
    clave = input("Introduce la clave: ")
print("Clave correcta")