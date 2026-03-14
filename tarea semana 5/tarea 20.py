def pedir_conjunto(mensaje):
    entrada = input(mensaje)
    return set(entrada.split())

def calcular_interseccion(set1, set2):
    return set1.intersection(set2)

print("--- 20. Intersección de Conjuntos ---")
print("Introduce los elementos separados por espacios.")

c1 = pedir_conjunto("Primer conjunto: ")
c2 = pedir_conjunto("Segundo conjunto: ")

interseccion = calcular_interseccion(c1, c2)

print("\nResultados:")
print(f"Conjunto 1: {c1}")
print(f"Conjunto 2: {c2}")
print(f"Intersección (elementos comunes): {interseccion}")