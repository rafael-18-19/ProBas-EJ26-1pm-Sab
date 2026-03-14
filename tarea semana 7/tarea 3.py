def contar_vocales(cadena):
    vocales = "aeiou"
    cadena = cadena.lower() # Convertimos todo a minúsculas para un conteo exacto
    resultado = []
    
    for vocal in vocales:
        cantidad = cadena.count(vocal)
        resultado.append((vocal, cantidad))
        
    return resultado

texto_usuario = input("Ingresa una cadena de texto para contar sus vocales: ")
conteo = contar_vocales(texto_usuario)
print(f"Conteo de vocales (vocal, apariciones): {conteo}")