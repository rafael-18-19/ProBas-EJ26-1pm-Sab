import math

r = float(input("Introduce el radio (r): "))
theta_grados = float(input("Introduce el ángulo (theta) en grados: "))

theta_rad = math.radians(theta_grados)

x = r * math.cos(theta_rad)
y = r * math.sin(theta_rad)

tupla_cartesiana = (round(x, 4), round(y, 4))
print(f"Coordenadas cartesianas (x, y): {tupla_cartesiana}")