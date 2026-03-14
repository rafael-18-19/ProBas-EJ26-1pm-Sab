diccionario = {}
while True:
    palabra_origen = input("Palabra original (o 'fin' para terminar de agregar): ")
    if palabra_origen.lower() == 'fin':
        break
    traduccion = input(f"Traducción de '{palabra_origen}': ")
    diccionario[palabra_origen] = traduccion

buscar = input("\nIngresa la palabra que deseas traducir: ")
if buscar in diccionario:
    print(f"Traducción: {diccionario[buscar]}")
else:
    print("Palabra no encontrada en el diccionario.")