# Descripción: programa que une dos listas y las ordena en orden ascendente.
lista1 = [1,2,3,4]
lista2= [5,6,7,8]

# Unir listas
lista1y2 = lista1 + lista2

# Orden ascendente
for num in lista1y2[::-1]:
    print(num)