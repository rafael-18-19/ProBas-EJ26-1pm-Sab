def invertir_cadena(texto):
    return texto[::-1]

if __name__ == "__main__":
    entrada = input("Ingresa una frase para invertir: ")
    resultado = invertir_cadena(entrada)
    print(f"Texto invertido: {resultado}")