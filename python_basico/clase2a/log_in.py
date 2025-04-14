# ------ Pedimos al usuario que introduzca una clave y verificamos si es correcta ------
clave = str(input("Introduce la clave: "))
# Convertimos la clave a minúsculas
clave = clave.lower()
# Verificamos SI(if) la clave es correcta
if clave == "12345abcdef":
    print("Clave correcta")
else:
    print("Clave incorrecta")
    # Solicitamos nuevamente la clave
    clave == input("Introduce la clave nuevamente: ")
    if clave == "12345abcdef":
        print("Clave correcta")
    else: 
        print("Clave incorrecta, numero de intenetos agotados")