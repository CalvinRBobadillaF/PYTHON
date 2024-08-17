import random

choices = ['piedra', 'papel', 'tijera']


name = input('Ingresa tu nombre guerrero: ')
print(f'Bienvenido {name} a piedra papel y tijeras!')

welcome = input('¿Quieres jugar contra el bot? (Si/No): ').lower()
if welcome == 'si':
    print('¡Genial! Vamos a empezar a jugar!')
    while True:
        computer_choice = random.choice(choices)
        user_choice = input('Elige entre piedra, papel o tijera... Buena suerte: ').lower()
        if user_choice not in choices:
            print('Opción inválida. Por favor, elige entre piedra, papel o tijera.')
            continue

        if user_choice == computer_choice:
            print('¡Empate! Intenta de nuevo.')
        elif (user_choice == 'piedra' and computer_choice == 'tijera') or \
             (user_choice == 'papel' and computer_choice == 'piedra') or \
             (user_choice == 'tijera' and computer_choice == 'papel'):
            print(f'¡Ganaste! {user_choice.capitalize()} vence a {computer_choice}.')
        else:
            print(f'¡Perdiste! {computer_choice.capitalize()} vence a {user_choice}.')

        play_again = input('¿Quieres jugar de nuevo? (Si/No): ').lower()
        if play_again != 'si':
            
            break
else:
    print('En ese caso, nos vemos miedoso!! jaja')