import random

# List of riddles and answers
riddles = [
    {"riddle": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "answer": "Fire"},
    {"riddle": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?", "answer":"A pencil lead"},
    {"riddle": "I am not alive, but I can die. I don't have wings, but I can fly. I don't have eyes, but I can see. What am I?", "answer":"A cloud"}
]

# Pick a random riddle
current_riddle = random.choice(riddles)

# Ask the riddle
guess = input(current_riddle["riddle"] + "\n")

# Check if the answer is correct
if guess.lower() == current_riddle["answer"].lower():
    print("¡Correcto!")
else:
    print("Incorrecto. La respuesta correcta es " + current_riddle["answer"])