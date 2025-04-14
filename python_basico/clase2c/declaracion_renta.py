monto = float(input("Ingrese el monto de la renta: "))
impositivo1 = 0.05
impositivo2 = 0.15
impositivo3 = 0.20
impositivo4 = 0.30
impositivo5 = 0.45
if monto >= 15000.00:
    if monto >= 15000.00 and monto <=25000.00:
        print("El monto a pagar (5%) es: ",monto*impositivo1)
    elif monto >= 25000.00 and monto <= 35000.00:
        print("El monto a pagar (15%) es: ",monto*impositivo2)
    elif monto >= 35000.00 and monto <= 60000.00:
        print("El monto a pagar (20%) es: ",monto*impositivo3)
    elif monto >= 60000.00:
        print("El monto a pagar (30%) es: ",monto*impositivo4)
else:
    print("No aplica impositivo")