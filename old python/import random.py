import random

# Lista de verbos en infinitivo
verbos = ["parler", "manger", "dormir", "jouer", "aller"]

# Lista de pronombres personales en francés
pronombres = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]

# Diccionario de conjugaciones de verbos en presente
conjugaciones_presente = {
    "parler": ["parle", "parles", "parle", "parlons", "parlez", "parlent"],
    "manger": ["mange", "manges", "mange", "mangeons", "mangez", "mangent"],
    "dormir": ["dors", "dors", "dort", "dormons", "dormez", "dorment"],
    "jouer": ["joue", "joues", "joue", "jouons", "jouez", "jouent"],
    "aller": ["vais", "vas", "va", "allons", "allez", "vont"]
}

# Seleccionar un verbo aleatorio de la lista
verbo = random.choice(verbos)

# Imprimir el verbo seleccionado
print("Conjugue el verbo: " + verbo)

# Iterar sobre los pronombres personales y mostrar su conjugación
for i in range(len(pronombres)):
    print(pronombres[i] + " " + conjugaciones_presente[verbo][i])
