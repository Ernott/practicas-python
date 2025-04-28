# Descripción: Encuentra los elementos duplicados de una lista, los borra y los coloca en otra. Luego
# Imprime la lista con los elementos únicos.

lista = [1,1,2,2,3,3,4,5,6]
lista_duplicados = []
lista_unica = []
for num in lista:
    if lista.count(num) > 1:
        if num not in lista_duplicados:
            lista_duplicados.append(num)
    else: 
        lista_unica.append(num)
print('Elementos unicos:', lista_unica)
print('Elementos duplicados;', lista_duplicados)