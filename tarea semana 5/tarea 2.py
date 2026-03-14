def invertir_letras_de_palabras(texto):
    palabras = texto.split()
    
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    
    resultado = " ".join(palabras_invertidas)
    
    return resultado


print("--- Bienvenid@ al Inversor de Palabras ---")

frase_usuario = input("Introduce la frase que quieras transformar: ")

frase_final = invertir_letras_de_palabras(frase_usuario)

print(f"\nResultado: {frase_final}")