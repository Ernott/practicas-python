# ----- Programa que solicita el nombre de usuario y verifica si el usuario se encuentra registrado en el sistema -----
# Pedimos el nombre de usuario
usuario = input('Ingrese su nombre de usuario: ')
# Eliminamos los caracteres especiales del nombre de usuario
usuario = usuario.replace('.', '').replace('#', '').replace(';', '').replace(':', '').replace(' ', '')
# Definimos los usuarios registrados en el sistema
usuario_1 = 'alejandro'
usuario_2 = 'naomi'
usuario_3 = 'sergio'
# Verificamos SI(if) el usuario se encuentra registrado en el sistema
if usuario.lower() == usuario_1 or usuario.lower() == usuario_2 or usuario.lower() == usuario_3:
    print('Hola ' , usuario.title() , ' bienvenido al sistema')
# En caso contrario(NO) imprimimos un mensaje de usuario no registrado
else:
    print('Usuario no registrado')