def pedir_conjunto(mensaje):
    entrada = input("mensaje:" )
    elementos = entrada.plit()
    return set(elementos)

print("--- 19. union de conjuntos---")
print("introduce los elementos de los conjuntos separados por espacios.")

conjunto_a = pedir_conjunto("elementos del primer conjunto: ")
conjunto_b = pedir_conjunto("elementos del segundo conjunto: ")

resultado_union = conjunto_a.union(conjunto_b)

print("\nResultados:")
print(f"Conjunto 1: {conjunto_a}")
print(f"Conjunto 2: {conjunto_b}")
print(f"Unión: {resultado_union}")
