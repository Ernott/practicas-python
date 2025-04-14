burger = str(input("Ingrese el tipo de hamburguesa (Vegana o clasica): "))
if burger.lower() == 'vegana':
    print("¿Que ingrediente desea agregar?")
    print("1. cebolla caramelizada")
    print("2. tofu")
    print("3. Sin ingredientes")
    ceb_caramelizada = '1'
    tofu = '2'
    ingrediente = input("Ingrese el ingrediente: ")
    if ingrediente == ceb_caramelizada:
        print("Hamburguesa vegana con cebolla caramelizada")
    elif ingrediente == tofu:
        print("Hamburguesa vegana con tofu")
    else:
        print("Hamburguesa vegana sin ingredientes")
elif burger.lower() == 'clasica':
    print("¿Que ingrediente desea agregar?")
    print("1. Queso Idiazabal")
    print("2. tocino")
    print("3. Huevos")
    print("4. Sin ingredientes")
    queso = '1'
    tocino = '2'
    huevos = '3'
    ingrediente = input("Ingrese el ingrediente: ")
    if ingrediente == queso:
        print("Hamburguesa clasica con Queso Idiazabal")
    elif ingrediente == tocino:
        print("Hamburguesa clasica con tocino")
    elif ingrediente == huevos:
        print("Hamburguesa clasica con huevos")
    else:
        print("Hamburguesa clasica sin ingredientes")
else:
    print("Tipo de hamburguesa no valido")