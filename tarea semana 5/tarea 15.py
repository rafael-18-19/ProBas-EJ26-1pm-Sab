filas = int(input("¿Cuántas filas tiene la matriz?: "))
matriz = [[int(x) for x in input(f"Fila {i+1} (números con espacio): ").split()] for i in range(filas)]

elemento = int(input("Introduce el elemento a buscar: "))
posiciones = []

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == elemento:
            posiciones.append((i, j))

if posiciones:
    print(f"Elemento encontrado en (fila, columna): {posiciones}")
else:
    print("El elemento no existe en la matriz.")