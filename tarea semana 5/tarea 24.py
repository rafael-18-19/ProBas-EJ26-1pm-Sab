print("--- 24. Verificación de Conjunto Vacío ---")

entrada = input("Introduce elementos para el conjunto (o pulsa Enter para dejarlo VACÍO): ")

mi_conjunto = set(entrada.split())

print(f"\nEl conjunto creado es: {mi_conjunto}")

if not mi_conjunto:
    print("El resultado es: El conjunto está VACÍO.")
else:
    print(f"El resultado es: El conjunto NO está vacío. Tiene {len(mi_conjunto)} elemento(s).")