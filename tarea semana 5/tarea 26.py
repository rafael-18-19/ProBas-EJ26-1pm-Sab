def pedir_conjunto(mensaje):
    entrada = input(mensaje)
    return set(entrada.split())

print("--- 26. Eliminación de Elementos ---")

mi_conjunto = pedir_conjunto("Introduce los elementos iniciales del conjunto (separados por espacio): ")

print(f"\nConjunto actual: {mi_conjunto}")

elemento_a_borrar = input("Introduce el elemento específico que quieres eliminar: ")



print(f"\nIntentando eliminar '{elemento_a_borrar}'...")
mi_conjunto.discard(elemento_a_borrar)


print(f"Conjunto final: {mi_conjunto}")