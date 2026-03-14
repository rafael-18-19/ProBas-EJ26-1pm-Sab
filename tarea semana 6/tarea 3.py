sinonimos_dict = {}
while True:
    palabra = input("Ingresa una palabra para agregar (o 'fin' para terminar registro): ")
    if palabra.lower() == 'fin':
        break
    sinonimos_input = input(f"Ingresa los sinónimos de '{palabra}' separados por coma: ")
    sinonimos_dict[palabra] = [s.strip() for s in sinonimos_input.split(',')]

buscar = input("\n¿Qué palabra deseas buscar?: ")
if buscar in sinonimos_dict:
    print(f"Sinónimos de {buscar}: {', '.join(sinonimos_dict[buscar])}")
else:
    print("La palabra no está en el diccionario.")

print("\n--- Claves disponibles en el diccionario ---")
for clave in sinonimos_dict.keys():
    print(clave)