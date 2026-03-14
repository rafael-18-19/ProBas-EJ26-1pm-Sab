puntajes = {}
while True:
    nombre = input("Ingresa el nombre del jugador (o escribe 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    puntaje = float(input(f"Ingresa el puntaje de {nombre}: "))
    puntajes[nombre] = puntaje

print("\n--- Registro Final de Puntajes ---")
for jugador, puntos in puntajes.items():
    print(f"Jugador: {jugador} | Puntaje: {puntos}")