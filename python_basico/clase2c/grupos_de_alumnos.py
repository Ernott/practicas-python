sexo = input("Ingrese el genero del alumno(F/M): ")
nombre = input("Ingrese el nombre del alumno: ")
f_a = 'EFGHIJKLM'
m_a = 'ABCDEFGH'
f_b = 'ABCDNOPQRSTUVWXYZ'
m_b = 'IJKLMNOPQRSTUVWXYZ'
if sexo == 'F':
    if nombre[0].upper() in f_a:
        print("El alumno pertenece al grupo A")
    elif nombre[0].upper() in f_b:
        print("El alumno pertenece al grupo B")
    else:
        print("El alumno no pertenece a ningun grupo")
elif sexo == 'M':
    if nombre[0].upper() in m_a:
        print("El alumno pertenece al grupo A")
    elif nombre[0].upper() in m_b:
        print("El alumno pertenece al grupo B")
    else:
        print("El alumno no pertenece a ningun grupo")
else:
    print("Genero no valido")