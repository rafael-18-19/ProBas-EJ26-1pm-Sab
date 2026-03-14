def limpiar_espacios(cadena):
    return " ".join(cadena.split())

entrada= input("introduce una cadena:")
resultado= limpiar_espacios(entrada)

print(f"resultado: '{resultado}'")