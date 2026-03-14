def contar_vocales_y_consonantes(palabra):
    vocales_referencia = "aeiouáéíóú"
    
    contador_vocales = 0
    contador_consonantes = 0
    
    palabra_limpia = palabra.lower()
    
    for letra in palabra_limpia:
        if letra.isalpha():
            if letra in vocales_referencia:
                contador_vocales += 1
            else:
                contador_consonantes += 1
                
    return contador_vocales, contador_consonantes


print("--- Analizador de Letras ---")
usuario_palabra = input("Ingresa una palabra para analizar: ")

v, c = contar_vocales_y_consonantes(usuario_palabra)

print(f"\nEn la palabra '{usuario_palabra}':")
print(f"* Vocales: {v}")
print(f"* Consonantes: {c}")