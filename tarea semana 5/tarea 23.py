print("--- 23. Eliminación de Duplicados ---")

entrada_usuario = input("Introduce una lista de palabras o números separados por espacios (incluye duplicados): ")

lista_original = entrada_usuario.split()

print(f"\nLista original (con duplicados): {lista_original}")


conjunto_sin_duplicados = set(lista_original)

print(f"Conjunto resultante (sin duplicados): {conjunto_sin_duplicados}")
