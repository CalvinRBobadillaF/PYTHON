name = 'Hola' + ' Calvin'
print(name)

print(type(name)) #es como si fuera el typeof de javascript.

comillas = """texto con comillas triples"""

#nueva info

print(name[2]) #con corchetes y el numero, podemos saber que letra tiene cada posicion

print(len(name))



prueba = 'soy un texto'
print(prueba.capitalize())
#Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas.
print(prueba.casefold())

#str.center(width[, fillchar])
#Retorna el texto de la cadena, centrado en una cadena de longitud width. El relleno a izquierda y derecha se realiza usando el carácter definido por el parámetro fillchar (por defecto se usa el carácter espacio ASCII). Si la cadena original tiene una longitud len(s) igual o superior a width, se retorna el texto sin modificar.

count = prueba.count('o') #sirve para contar cuantas veces aparece cierta palabra en un texto. 
print(count)

titulo = prueba.title() #es como capitalize, pero es cada palabra separada por espacios del texto la que me devuelve en mayuscula.
print(titulo)

print(prueba.swapcase()) #swapcase me devuelve el texto invertido, lo que esta en mayus pasa a minus y viceversa.

reemplazo = prueba.replace('soy', 'Esto') #reempleza una palabra del texto por una nueva, primero la vieja, luego la nueva.

print(reemplazo)


#Integer, booleans 

x = 10
z = 3.1416
y = 523.21e6
print(type(x)) 
print(x + y)

a = True
b = False
print(a + b) #si a es true y b es false, a + b es 1

#Si tenemos 10 y lo sumamos a 10.0, el resultado sera 20,0, sigue siendo un flotante, hay que tener en cuenta eso

#PRINT

print("Soy un texto") #texto plano normal
print("Soy" + "un" + "texto") #Al usar + no se anade espacio, hay que
#agregarlo manualmente

print ('soy', 'un', 'texto') #Al usar comas si se anade el espacio.

print('Soy', 'un', 'texto', sep=',') #con sep, podemos indicar como queremos que se separe el texto
#que se imprime.

#print('Nunca', end=" ")
#print('pares de aprender', end=" ") #con end lo que hacemos es pegar
#2 texto, mediante los espacios.

#f-strings, son como los `` de javascript, nos permiten insertar
#variables entre corchetes y usar sus datos


texto = 'Soy unu texto'
otroTexto = 'Soy otro texto'

print(f'Esto dice: {texto}, y esto otro: {otroTexto}')

#Otro que puede ser util en backend, es imprimir en formato especifico
#osea, un numero grande se puede redondear directamente en print

valor = 3.14159
print("Valor: {:.2f}".format(valor)) #con {:.2f} especificamos
#cuantos decimales queremos que imprima.

#con \n podemos especificar saltos de linea

print('Esto es un\nsalto de linea')

print('Hola! soy \'calvin\'') #Con \ podemos agregar elementos especiales
#como las comillas

#Operaciones aritmeticas: esto ya me lo sabia, pero es bueno darle un
#repaso

#Suma: a + b

num = 15
num2 = 5

print(num + num2)
#Resta: a - b

print(num - num2)

print(num * num2)

print(num / num2)

#MODULO lo que sobra de una division impar

print(num % num2)

print(num ** num2)

print(num // num2) #En caso de que sea impar, con doble / indicamos que
#divida pero que redondee a un entero

#Ejemplo de uso de modulo
#Si tenemos un dia de la semana y queremos saber el dia siguiente
#podemos usar el modulo
dia = 3 #3 es martes
diaSiguiente = (dia + 1) % 7 #7 es el numero de dias
#de la semana
print(diaSiguiente)

#Ademas, podemos usar shortcuts, que son formas de escribir codigo
#simplificado, cuando vayamos a hacer una operacion, podemos ahorrar
#lineas de codigo:


prueba = int(input('Ingresa cualquier cosa:'))
print(prueba)
print(type(prueba))

#Ejemplo de uso de shortcuts
#Si tenemos dos variables y queremos sumarlas y multiplicarlas
#Podemos hacerlo de la siguiente manera:



print(num) #nos devuelve 35 sin hacer num mas directamente el numero.and
#y se puede hacer con todos los signos, mientras este antes del igual.
#ademas, python sigue el orden de sus operaciones por PEMDAS.

z = num + num2
print(z) #nos devuelve 20

#Ultima parte de este archivo: Entradas y salidas de informacion con
#python

#podemos usar input pedirle a un usuario mediante la consola
#que ingrese informacion:

nombre = input('Hola!, cual es tu nombre?: ')
edad = int(input('cual es tu edad?: '))
#int es un tipo de dato que nos permite convertir un string a un number
Actions = input('Que andas estudiando ahora?: ')

message = (f"""Hola! {nombre}, esta es una prueba para crear mensajes 
con f-strings y usando input. Tu edad es {edad} y estas estudiando {Actions}.""")

print(message)