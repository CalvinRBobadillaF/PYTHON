import random


def adivinar_numero_humano():
    print("""
    
Ahora será tu turno.""")
    numero = random.randint(1,100)
    numero_adivinado = int(input("""
Adivina el número que he pensado: """))
    intentos = 1
    while numero_adivinado != numero:
        intentos += 1
        if numero < numero_adivinado:
            numero_adivinado = int(input("Pon un número menor: "))
        else:
            numero_adivinado = int(input("Pon un número mayor: "))
    print("""
    Has adivinado mi número en un total de """ + str(intentos) + " intentos.")
    return intentos


def adivinar_numero_maquina():
    inicio=''
    print("""
Adivinaré el número que estás pensando.
    """)
    while inicio != 'ya':
        inicio = input("Piensa un número del 1 al 100 y cuando lo tengas escribe ya: ")
    print("""
    Para saber si he adivinado tu número o no pon lo siguiente:
    1. Si el número que pensaste es mayor al que mande.
    2. Si el número que pensaste es menor al que mande.
    3. Si el número es correcto.    
    """)
    opcion = 0
    lim_inferior = 1
    lim_superior = 100
    numero_pensado = random.randint(lim_inferior,lim_superior)
    intentos = 0
    while opcion != 3:
        opcion = int(input("El número que pensaste fue " + str(numero_pensado) +  ": "))
        intentos += 1
        if opcion == 1:
            lim_inferior = numero_pensado + 1
        elif opcion == 2:
            lim_superior = numero_pensado - 1
        numero_pensado = random.randint(lim_inferior,lim_superior)
    print("""
    He adivinado tu número en un total de """ + str(intentos) + " intentos.") 
    return intentos

def run():
    intentos_pc = adivinar_numero_maquina()
    intentos_humano = adivinar_numero_humano()
    if intentos_pc < intentos_humano:
        print("""
    Jeje te he ganado, soy una maquina nunca pierdo""")
    elif intentos_humano < intentos_pc:
        print("""
    Has tenido algo de suerte, me has ganado...""")
    else:
        print("""
    Al parecer quedamo empate.""")

if __name__ == '__main__':
    run()