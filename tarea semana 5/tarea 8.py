entrada = input("introduce una lista de palabras separadas por espacios: ")
palabras = entrada.split()

palabras.sort(key=len)

print(f"palabras ordenadas por longitud: {palabras}")