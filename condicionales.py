#obviamente es un tema que ya mas o menos se pero es bueno repasarlo:

x = 10
y = 5

if x > y:
    print("x es mayor que y")
elif x < y:
     print('x es menor que y')
else:
    print("x es igual a y")


#porfinn, el && de python es literalmente and, en vez de siimbolos es la
#palabra.

#OR para si una condicion se cumple o si esta otra se cumpla, has esto.

#not es para negar, si algo no se cumple

#Los if anidados son if dentro de otros if, es util para que en caso
#de que una condicion grande como trues o falses se cumplen o no,
#tome un camino, y los elif ya son para una misma considicion

if x and y > 10:
    print("x es verdadero y y es mayor que 10")
else:
    print('x o y no son mayores que 10.')

if not x > 10:
    print("x no es mayor que 10")
else:
    print('x es mayor que 10')

if x or y > 19:
    print('x o y son mayores que 19')
else:
    print('alguno de ellos no son mayores que 19')