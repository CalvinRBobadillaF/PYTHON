import random

words = ['python', 'javascript', 'react', 'django', 'fullstack']

randomWord = random.choice(words)
print(f'para ayudarte y para la prueba, la palabra es: {randomWord}')
userGuess = input('adivina la palabra! es un lenguaje de programacion o un framework:')

if userGuess == randomWord:
    print(f'¡felicidades! adivinaste la palabra {randomWord}')
else:
    print('sorry, intentalo de nuevo')