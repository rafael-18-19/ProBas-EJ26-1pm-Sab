def pedir_conjunto(mensaje):
    entrada = input(mensaje)
    return set(entrada.split())

def es_subconjunto(posible_sub, conjunto_mayor):
    return posible_sub.issubset(conjunto_mayor)

print("--- 22. Comprobación de Subconjunto ---")
print("Introduce los elementos separados por espacios.")

conjunto_1 = pedir_conjunto("ingresa el primer conjunto: ")
conjunto_2 = pedir_conjunto("ingresa el segundo conjunto: ")
if es_subconjunto(conjunto_1, conjunto_2):
    print(f"\nEl primer conjunto {conjunto_1} si es un conjunto de {conjunto_2}")
elif es_subconjunto(conjunto_2, conjunto_1):
    print(f"\nEl segundo conjunto {conjunto_2} SÍ es un subconjunto de {conjunto_1}.")
else:
    print("\nNinguno de los conjuntos es subconjunto del otro.")