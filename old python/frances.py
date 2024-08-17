import random

# Diccionario de verbos y conjugaciones en presente
verbos_presente = {
    "parler": ["parle", "parles", "parle", "parlons", "parlez", "parlent"],
    "manger": ["mange", "manges", "mange", "mangeons", "mangez", "mangent"],
    "dormir": ["dors", "dors", "dort", "dormons", "dormez", "dorment"],
    "jouer": ["joue", "joues", "joue", "jouons", "jouez", "jouent"],
    "aller": ["vais", "vas", "va", "allons", "allez", "vont"]
}

# Seleccionar un verbo aleatorio del diccionario
verbo = random.choice(list(verbos_presente.keys()))

# Imprimir el verbo seleccionado
print("Conjuguer le verbe : " + verbo)

# Pedir al usuario que conjugue el verbo en presente
for i in range(len(verbos_presente[verbo])):
    pronombre = input("Conjuguer le verbe pour '" + verbos_presente[verbo][i] + "': ")
    if pronombre != verbos_presente[verbo][i]:
        print("Je suis désolé! La conjugaison correcte pour '" + verbos_presente[verbo][i] + "' es: " + verbos_presente[verbo][i] + " " + verbo)
        exit()

# Si el usuario ha conjugado el verbo correctamente, felicitarlo
print("Félicitations! Vous avez correctement conjugué le verbe '" + verbo + "' dans le présent.")
