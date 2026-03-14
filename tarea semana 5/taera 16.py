print("Introduce los datos para la matriz de 5x5:")
matriz = [[int(x) for x in input(f"Fila {i+1} (5 números con espacio): ").split()] for i in range(5)]

suma_principal = sum(matriz[i][i] for i in range(5))
suma_secundaria = sum(matriz[i][4 - i] for i in range(5))

print(f"Suma de Diagonal Principal: {suma_principal}")
print(f"Suma de Diagonal Secundaria: {suma_secundaria}")
print(f"Suma Total de diagonales: {suma_principal + suma_secundaria}")