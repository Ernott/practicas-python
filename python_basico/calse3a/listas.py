frutas = [ 'manzana', 'platano', 'cereza' , 'pera', 'higo' , 'frambuesa', 'fresa' ]
print(len(frutas))
print(frutas[2])
frutas[1] = 'mora'
frutas.append('mango')
frutas.insert(0,'uva')
for i in frutas:
    print(i)
ultima_fruta = str(frutas[-1])
frutas.pop()
print('quite esa verga xd ', ultima_fruta, ' de esta mierda ' ,frutas)