Menu = """Bienvenido al convertor de monedas


1 - Pesos Dominicanos
2 - Pesos Mexicanos
3 - Pesos Brasileños

Cual opcion eliges: """

opcion = int(input(Menu))

if opcion == 1:
    Pesos = input("Cuantos pesos dominicanos tienes:")
    Pesos = float(Pesos)
    valor_dolar = 52
    Dolares = Pesos / valor_dolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print("Tienes $" + Dolares + " Dolares ")
elif opcion == 2:
    Pesos = input("Cuantos pesos mexicanos tienes:")
    Pesos = float(Pesos)
    valor_dolar = 20
    Dolares = Pesos / valor_dolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print("Tienes $" + Dolares + " Dolares ")
elif opcion == 3:
    Pesos = input("Cuantos pesos tienes:")
    Pesos = float(Pesos)
    valor_dolar = 10
    Dolares = Pesos / valor_dolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print("Tienes $" + Dolares + " Dolares ")
else: print("Elige una opcion correcta")








