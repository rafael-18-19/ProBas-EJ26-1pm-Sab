print("Introduce los datos para la matriz de 3x3:")
matriz = [[int(x) for x in input(f"Fila {i+1} (3 números con espacio): ").split()] for i in range(3)]

transpuesta = [[matriz[j][i] for j in range(3)] for i in range(3)]

print("\nMatriz Transpuesta:")
for fila in transpuesta:
    print(fila)