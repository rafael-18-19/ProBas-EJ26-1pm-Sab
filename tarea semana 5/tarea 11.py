n = int(input("ingrese el numero de filas (n): "))
m = int(input("introduce el numero de columnas (m): "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append((i + j) % 2)
        matriz.append(fila)

print("matris resultante:")
for fila in matriz:
    print(fila)