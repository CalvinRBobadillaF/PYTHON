
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?")
    pesos = float(pesos)
    Dolares = pesos / valor_dolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print("Tienes $" + Dolares + "Dolares")

Menu = """Bienvenido al convertor de monedas


1 - Pesos Dominicanos
2 - Pesos Mexicanos
3 - Pesos Brasileños

Cual opcion eliges: """

opcion = int(input(Menu))

if opcion == 1:
    conversor("Dominicanos", 52)
elif opcion == 2:
    conversor("Mexicanos", 24)
elif opcion == 3:
   conversor("Brasileños", 10)
else: print("Elige una opcion correcta")