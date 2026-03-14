texto = input("Ingresa un párrafo o texto largo: ")
palabras = texto.lower().split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencias.items():
    print(f"'{palabra}': {cantidad} veces")