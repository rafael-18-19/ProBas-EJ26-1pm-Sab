def ordenar_palabras(lista_palabras):
    return sorted (lista_palabras)

entrada = input("ingresa varias palabras separadas por espacios: ")
palabras = entrada.split()

palabras_ordenadas = ordenar_palabras(palabras)
print(f"palabras ordenadas alfabeticamente: {palabras_ordenadas}")