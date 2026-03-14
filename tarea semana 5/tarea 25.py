def obtener_conjunto_consonantes(cadena):
    """Crea la función solicitada."""
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    consonantes_presentes = set()
    
    texto_limpio = cadena.strip()
    
    for caracter in texto_limpio:
        if caracter.isalpha() and caracter not in vocales:
            consonantes_presentes.add(caracter.lower())
            
    return consonantes_presentes

print("--- 25. Palabras sin Vocales (Consonantes) ---")

texto_usuario = input("Introduce una palabra, frase o cadena de texto: ")

conjunto_resultante = obtener_conjunto_consonantes(texto_usuario)

print(f"\nTexto original: '{texto_usuario}'")
print(f"Conjunto de consonantes únicas presentes: {conjunto_resultante}")