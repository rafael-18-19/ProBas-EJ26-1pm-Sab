import random

def iniciar_juego():
    print("--- Juego de Adivinanza ---")
    print("He generado un número aleatorio entre 1 y 100.")
    print("¡Intenta adivinarlo!")
    
    numero_secreto = random.randint(1, 100)
    adivinanza = -1
    intentos = 0

    while adivinanza != numero_secreto:
        try:
            entrada = input("Tu intento: ")
            adivinanza = int(entrada)
            intentos += 1

            if adivinanza < numero_secreto:
                print("-> El número es MAYOR.")
            elif adivinanza > numero_secreto:
                print("-> El número es MENOR.")
            else:
                print(f"¡CORRECTO! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

iniciar_juego()