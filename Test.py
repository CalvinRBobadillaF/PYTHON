import random
choices = ['piedra', 'papel', 'tijera']

computerChoice = random.choice(choices)
userName = input('Cual es tu nombre?:')
userInput = input(f'Bienvenido {userName} a piedra papel y tijeras, elige una opcion!: ')


if userInput == computerChoice:
    print(f'Empate, {userName} y la computadora eligieron {userInput}')
elif (userInput == 'piedra' and computerChoice == 'tijera') or \
             (userInput == 'papel' and computerChoice == 'piedra') or \
             (userInput == 'tijera' and computerChoice == 'papel'):
    print(f'Ganaste! tu {userInput} le gana a {computerChoice}')
else:
    print(f'perdiste, {computerChoice} le gana a tu {userInput}')




def calcularTiempo(horas, dinero, dias):
    ingresos = horas * dinero * dias
    print(f'Ganaria de ser asi {ingresos} en total')
# Calcula el tiempo que tarda en ganar el dinero ingresado



calcularTiempo(11,13,56)


def convertirDiasEnHoras(dias):
    horas = dias * 24
    print(f'{dias} dias son en total {horas} horas')

convertirDiasEnHoras(74)
    



