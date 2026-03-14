entrada = input("introduce una lista de numeros separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

pares = [num for num in numeros if num % 2 == 0]

print(f"lista filtrada (solo pares): {pares}")