def es_palindromo(texto):
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print("¡Es un palíndromo!")
    else:
        print("No es un palíndromo.")