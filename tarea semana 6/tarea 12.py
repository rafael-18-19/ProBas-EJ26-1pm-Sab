estudiantes = {}

while True:
    nombre = input("Nombre del estudiante (o 'fin' para salir): ")
    if nombre.lower() == 'fin':
        break
    
    asignaturas = {}
    print(f"--- Asignaturas de {nombre} ---")
    while True:
        materia = input("Nombre de la materia (o 'listo' para terminar materias): ")
        if materia.lower() == 'listo':
            break
        calif = float(input(f"Calificación en {materia}: "))
        asignaturas[materia] = calif
    
    amigos_input = input("Ingresa los nombres de sus amigos separados por coma: ")
    amigos = [amigo.strip() for amigo in amigos_input.split(',')]
    
    estudiantes[nombre] = {
        "asignaturas": asignaturas,
        "amigos": amigos
    }

print("\n--- Información Completa de Estudiantes ---")
for nombre, datos in estudiantes.items():
    print(f"\nEstudiante: {nombre}")
    print(f"Asignaturas y Notas: {datos['asignaturas']}")
    print(f"Lista de amigos: {datos['amigos']}")