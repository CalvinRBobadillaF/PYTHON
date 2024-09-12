#Llegamos a los ciclos, igual que cualquier otro lenguaje, tenemos el for
#El ciclo for se  utiliza para recorrer una lista o un strings etc. Consta del famoso
#variable i
#i es la variable donde se guarda esa informacion. Si queremos acceder a esa info, debemos
#acceder a i

numbersList = [1,2,3,4,5,6]

#para iterarla

for i in numbersList:
    print(i + i)
    print(i + 1)

#si sumamos, o hacemos algun metodo con i, este afectara a todos los datos.abs
#ademas si hacemos console de 2 i, o de listas, se imprimira primero un dato de 1 lista,
#y luego otro dato de otra lista.

#Por otra parte con range podemos crear listas, desde un tipo de elemento hasta otro tipo de
#dato o elemnto


for i in range(10): #inicia en 0 y termina en 9
    print(i)

for i in range(2,13): #primer valor iniicio, segundo valor el final -1
    print(i)

for i in range('a','n'): #da error, solo se puede hacer con numeros
    print(i)

randomList = list(range('a','x')) #se pueden crear con for, pero solo con numeros.

print(randomList)

#otra forma de iterar (igual que en JS obvio), es con for x elemento en x elemento

programmingLenguajes = ['python', 'javascript', 'c#', 'java', 'c++', 'c','cobol']

for lenguajes in programmingLenguajes:
    print(lenguajes)
    if lenguajes == 'python':
        print(lenguajes)

#ahora si, llegamos a while. While obviamente significa que mientras una condicion se cumpla
#ejecute el siguiente codigo

x = 1

while x > 0: #como x no es mayor que 10, no hace nada pero si fuera igual o menor, lo imprimiria
    print(x)
    x += 1 #para sumar x
    if x == 1000:
        break

    # con break, podemos indicar que si se cumple una condicion, una vez se cumpla se termine