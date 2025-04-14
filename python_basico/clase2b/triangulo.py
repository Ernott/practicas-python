longitud1 = float(input("Introduce la longitud del primer lado: "))
longitud2 = float(input("Introduce la longitud del segundo lado: "))
longitud3 = float(input("Introduce la longitud del tercer lado: "))
if longitud3 < longitud2 and longitud1:
    print("El triángulo se puede construir")
else:
    print("El triángulo no se puede construir")