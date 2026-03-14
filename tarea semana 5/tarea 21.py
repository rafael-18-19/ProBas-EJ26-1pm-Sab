def pedir_conjunto(mensaje):
    entrada = input(mensaje)
    return set(entrada.plit())

print("--- 21. Diferencia entre Conjuntos ---")
print("Introduce los elementos separados por espacios.")
print("(Recuerda: Diferencia A - B son elementos en A que NO están en B)")

conjunto_a = pedir_conjunto("primer conjunto (A): ")
conjunto_b = pedir_conjunto("segundo conjunto (b): ")

diferencia_a_b = conjunto_a.difference(conjunto_b)

diferencia_a_b = conjunto_b - conjunto_a

print("\nResultados:")
print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"Diferencia (A - B): {diferencia_a_b}")