import math

print("--- Punto 1 ---")
x1, y1 = [float(val) for val in input("Introduce x1 e y1 separados por espacio: ").split()]

print("--- Punto 2 ---")
x2, y2 = [float(val) for val in input("Introduce x2 e y2 separados por espacio: ").split()]

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia euclidiana entre los puntos es: {round(distancia, 4)}")