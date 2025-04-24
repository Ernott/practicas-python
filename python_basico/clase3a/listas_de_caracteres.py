# 1. Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas 
# de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa.

frutas = ['manzana', 'platano', 'cereza', 'pera', 'higo', 'frambuesa', 'fresa']

# 2. Usa la función len() para imprimir la longitud de la lista frutas.

print('La longitud de la lista frutas es de', len(frutas))

# 3. Accede al objeto numero 3 de la lista e imprímelo or consola.

print('El objeto 3 de la lista frutas es', frutas[2])

# 4. Modifica el segundo objeto de la lista y cambiado a mora

frutas[1]='mora'
print('El objeto 2 de la lista frutas es', frutas[1])

# 5. Añade el string mango al final de la lista

frutas.append('mango')
print('El nuevo objeto es', frutas[7])

# 6. Usa el método insert() y añade el string “uva“ año comienzo de la lista. 

frutas.insert(0,'uva')
print('El objeto 0 es', frutas[0])

# 7. Usa un bucle para recorrer la lista e imprimir cada fruta por la consola 

print('Recorriendo la lista frutas con un bucle: ')
for fruta in frutas:
    print(fruta)

# 8. Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable 
# llamada “ultima_fruta“.

ultima_fruta = frutas.pop()
print('La ultima fruta eliminada es', ultima_fruta)

# 9. Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola

print('Recorriendo la lista frutas con un bucle: ')
for fruta in frutas:
    print(fruta)

# 10. Modifica el script para que imprima también la longitud de cada nombre de fruta por consola

print('Recorriendo la lista frutas y cada letra con un bucle: ')
for fruta in frutas:
    print('Deletreare la fruta', fruta)
    for letra in fruta:
        print(letra)

# 11. Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que 
# tengan más de 5 caracteres

for fruta in frutas:
    if len(fruta) >= 5:
        print('La frutas deletreadas mayor a 5 caracteres son: ')
        print(fruta)

# 12. Usa el método remove() para borrar el string “cereza“ de la lista.

frutas.remove('cereza')
print(frutas)

# 13. Usa el método clear() para vaciar la lista.

frutas.clear()
print(frutas)