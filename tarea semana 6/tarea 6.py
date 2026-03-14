estudiantes = {}
while True:
    nombre = input("Nombre del estudiante (o 'fin' para salir): ")
    if nombre.lower() == 'fin':
        break
    notas_str = input("Ingresa las calificaciones separadas por espacio: ")
    notas = [float(nota) for nota in notas_str.split()]
    estudiantes[nombre] = notas

print("\n--- Registro de Estudiantes y Notas ---")
for nombre, notas in estudiantes.items():
    print(f"{nombre}: {notas}")