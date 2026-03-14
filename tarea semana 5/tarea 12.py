print("--- datos para la matriz 1 ---")
m1 = [[int(x) for x in input(f"fila {i+1} (3 numeros con espacio): ").split()]for i in range(3)]

print("--- datos para la matriz 2 ---")
m2 = [[int (x) for x in input(f"fila {i+1} (3 numeros con espacio): ").split()] for i in range(3)]

suma = [[m1[i][j] + m2[i][j] for j in range(3)] for i in range(3)]

print("\nMatriz suma: ")
for fila in suma:
    print(fila)