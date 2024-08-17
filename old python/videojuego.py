import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Entrez un nombre compris entre 1 et 100: "))
    while numero_elegido != numero_aleatorio: 
        if numero_elegido < numero_aleatorio:
            print("Tu á choisi un petit nombre")
        
        else:
            print("Tu á choisi un plus grand nombre")
        numero_elegido = int(input("Essayez un autre numéro : "))
    print("Won pibe")


if __name__ == "__main__":
    run()