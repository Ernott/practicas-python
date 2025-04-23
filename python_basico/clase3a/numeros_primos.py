# imprimimos por pantalla los numeros primos del 2 al 100
# Creamos un bucle que recorra el rango de números del 2 al 100
for i in range(2,101):
    # Creamos una variable que contenga el valor True
    es_primo = True
    # Creamos un bucle que recorra el rango de números del 2 al i
    for j in range(2,i):
        # Creamos una condición que valide si el número i es divisible por j
        if i % j == 0:
            # Si el número i es divisible por j, la variable es_primo toma el valor False
            es_primo = False
    # Creamos una condición que valide si la variable es_primo es True
    if es_primo == True:
        # Si la variable es_primo es True, imprimimos por pantalla el número i
        print(i)