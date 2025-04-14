#----- Programa que solicite una contraseña segura al usuario y verifique si la contraseña es segura -----
# Pedimos la contraseña al usuario
clave = input('Ingrese su contraseña: ')
clave = str(clave)
# Definimos las condiciones que debe cumplir la contraseña
# La contraseña debe tener una vocal en minuscula y dos caracteres especiales diferentes (*, #)
if ('a' in clave or 'e' in clave or 'i' in clave or 'o' in clave or 'u' in clave) and ('*' in clave or '#' in clave):
    print('Contraseña segura')
# En caso contrario imprimimos un mensaje de contraseña no segura
else:
    print('La contraseña debe tener al menos una vocal en minuscula y dos caracteres especiales diferentes (*, #)')