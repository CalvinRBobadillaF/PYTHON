#LISTAS
#ARRAYS tambien pueden ser llamadas:



#crear array:

array = ['Soy', 'un array', 'con varios tipos de datos: ', 23, 'number', True, False, 'o booleans']
array.append(6)
print(array)

mix = ['RE-MIX', 20, 3.1416, True, ['Soy una lista dentro de otra lista XDD', 19], 10]
print(mix)
print(type(mix))
print(len(mix)) #recuerda, con len podemos ver la longitud igual que lenght.
print(mix[0]) #acceder a un elemento de la lista especifico

print('El primer elemento de la lista, su indice es 0', mix[0])

#Podemos acceder a pedazitos de elementos en un array de la siguiente forma

print(mix[0:3]) #Hay que tener en cuenta, que no son los 3 elementos q siguen
#son los 3 primeros elementos, si queremos los 3 ultimos, usamos -3
#ademas, al igual que en otro lenguaje idk why, es el numero que pongamos -1
#osea que no es del 0 al 3, es del 0 al 2.

#Con append podemos agregar datos pero estos siempre se agregan
#al final de la lista, pero con INSERT podemos agregarlos a un lugar
#especifico, let's check that

mix.insert(1, 'Dato que vas a insertar (boolean, str, int, o list)')
print(mix)

#con index, podemos buscar en que posicion se encuentra cierto elemento:

print(mix.index(20)) #pero solamente devuelve la primera aparacion
#si hay datos repetidos, me devolvera la posicion del primero que hayo el.

#Si tenemos una lista con numero, podemos saber cual es el numero mayor o menor.abs
numbers = [20, 40, 60, 70 ,0.2120, 293232]
print(max(numbers))

#lo mismo pero con min

print(min(numbers))

#con la palabra reservada del podemos eliminar datos de listas.abs

del numbers[3]
print(numbers)

#cuando creamos una lista, y mediante otra variable le asignamos el
#valor de esa lista, hay que tener cuidado ya que la nueva variable
#que creamos apunta al mismo espacio en memoria que la lista original
#en otras palabras, si algo cambia en la lista original
#la copia tambien.

#con print(id(variable)) podemos saber el id, o el espacio en memoria
#de una variable.

x = [1,2,3,4,5] #mismo id
y = x #mismo id

z = x[:] #distinto id
x.append(6)

#TUPLAS
#Volvemos con las tuplas, las tuplas son un tipo de dato (no digo lista
#pero se parecen) inmutables, cuando se crean, su valor no se puede
#reasignar.


tupla = (1,2,3,4,5) #esto es una tupla, sus datos no cambian
#a no ser que directamente se lo asignemos

#Tambien podemos crear matrices en python mediante arrays dentro de arrays

matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9]
             ]

print(matrix)


#DICCIONARIOS: Su sintaxis es exactamente igual que los objetos en JS
#la diferencia es que los diccionarios son como su nombre lo dice
#guardar informacion mediante clave-valor

#xample:

information = {
    "name": "Calvin",
    "age": 18,
    "height": 1.70,
    "Profession": 'Full stack developer'

}
# que no se te olvide, para eliminar datos no dique dato.del, hay una
#palabra reservada para ello, del

del information["height"]
print(information)

#a diferencia de las listas, aqui eliminamos datos directamente por su
#nombre dentro de los corchetes.

#Para acceder a las claves o keys, usamos la propiedad .keys

claves = information.keys()
values = information.values()
print(claves, values)
print(type(claves), type(values))
print(claves)

#Con keys accedemos a su llave o propiedad, con values a su valor..
#pero con items accedemos a ambos dividios en tuplas.

print(information.items()) #con eso imprimimos key - value dentro de tuplas

#No son objetos, lo que pasa es que como aprendi javascript en serio de
#primero, convierto o referencio todo asi XDD. pero basicamente,
#podemos crear diccionarios dentro de diccionarios para dividir info

contact = { 'Calvin': {
    'age': 18,
    'height': 1.70,
    'Profession': 'Full stack developer',
    'Hobbies': 'Play chess and learn python',
    'Message': 'I study javascript as my professional lenguaje, and the lenguaje than i will become expert. But i looove python 10x times more than JS'

},  'Anderson': {
    'age': 18,
    'height': 1.77,
    'Profession': 'for now chef, but in the future i will be a minister or president',
    'Hobbies': 'Play soccer and idk, maybe maths?? (im not sure)',
    'message': 'Why did you have to move to portugal??...'
}


}

print(contact['Calvin'].items())


# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)