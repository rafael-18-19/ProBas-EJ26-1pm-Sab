peliculas = {}

print("--- Registro de Películas ---")
while True:
    nombre = input("Ingresa el nombre de la película (o escribe 'fin' para salir): ")
    if nombre.lower() == 'fin':
        break
    
    generos_input = input(f"Ingresa los géneros de '{nombre}' separados por coma: ")
    generos = [g.strip() for g in generos_input.split(',')]
    
    actores_input = input(f"Ingresa los actores principales separados por coma: ")
    actores = [a.strip() for a in actores_input.split(',')]
    
    peliculas[nombre] = {
        "generos": generos,
        "actores": actores
    }

print("\n--- Catálogo Final de Películas ---")
for nombre, info in peliculas.items():
    print(f"\n🎬 Película: {nombre}")
    print(f"   Géneros: {', '.join(info['generos'])}")
    print(f"   Actores: {', '.join(info['actores'])}")