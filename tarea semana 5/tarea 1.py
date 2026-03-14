def contar_palabras(texto):
   
    palabras = texto.split()
    return len(palabras)


print("--- Bienvenido al contador de palabras ---")

parrafo_usuario = input("Por favor, escribe o pega tu texto aquí y presiona Enter: ")

total = contar_palabras(parrafo_usuario)

print(f"\n¡Listo! El texto que introdujiste tiene {total} palabras.")