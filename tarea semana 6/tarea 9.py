import math

puntos = []
cantidad = int(input("¿Cuántos puntos vas a ingresar?: "))

for i in range(cantidad):
    x = float(input(f"Coordenada X del punto {i+1}: "))
    y = float(input(f"Coordenada Y del punto {i+1}: "))
    puntos.append((x, y))

def distancia_origen(punto):
    return math.sqrt(punto[0]**2 + punto[1]**2)

puntos_ordenados = sorted(puntos, key=distancia_origen)

print("\n--- Puntos ordenados por cercanía al origen ---")
for p in puntos_ordenados:
    print(f"Punto {p} - Distancia: {distancia_origen(p):.2f}")