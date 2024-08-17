Menu = """Bienvenido al conversor de monedas
Elige una opcion:

1 - Pesos dominicanos
2 - Pesos Mexicanos
3 - Pesos Brasileños

Elige una opcion: 
"""
opcion = input(menu)

if opcion == 1:
    pesos = input("cuantos pesos dominicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 52
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
elif opcion == 2:
    pesos = input("cuantos pesos mexicanos tienes?")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
else opcion == 3:
    pesos = input("cuantos pesos Brasileños tienes?: ")
    pesos = float(pesos)
    valor_dolar = 10
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares" )
