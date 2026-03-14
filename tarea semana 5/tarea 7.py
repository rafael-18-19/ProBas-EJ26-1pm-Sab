nombre_completo= input("introduce el nombre completo (ej. abel juarez murga): ")

iniciales = "".join([palabra[0].upper() for palabra in nombre_completo.split() if palabra])

print(f"tus inicuales son: {iniciales}")