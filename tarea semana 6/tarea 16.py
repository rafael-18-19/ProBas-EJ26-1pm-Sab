paises = {}

print("--- Registro Geográfico de Países ---")
while True:
    nombre_pais = input("\nIngresa el nombre del país (o 'fin' para salir): ")
    if nombre_pais.lower() == 'fin':
        break
    
    ciudades_input = input(f"Ingresa las ciudades importantes de {nombre_pais} separadas por coma: ")
    ciudades = [c.strip() for c in ciudades_input.split(',')]
    
    lista_coordenadas = []
    print("A continuación, ingresa las coordenadas de cada ciudad:")
    
    for ciudad in ciudades:
        print(f"📍 {ciudad}:")
        lat = input("   Latitud: ")
        lon = input("   Longitud: ")
        
        lista_coordenadas.append({"latitud": lat, "longitud": lon})
    
    paises[nombre_pais] = {
        "ciudades_importantes": ciudades,
        "coordenadas": lista_coordenadas
    }

print("\n--- Información Geográfica Recopilada ---")
for pais, datos in paises.items():
    print(f"\n🌎 País: {pais}")
    # Usamos zip para emparejar cada ciudad con su respectivo diccionario de coordenadas
    for ciudad, coord in zip(datos["ciudades_importantes"], datos["coordenadas"]):
        print(f"  - {ciudad}: [Latitud: {coord['latitud']}, Longitud: {coord['longitud']}]")