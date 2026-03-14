alumnos = []
while True:
    nombre = input("Nombre del alumno (o 'fin' para salir): ")
    if nombre.lower() == 'fin':
        break
    edad = int(input("Edad: "))
    calificaciones = input("Calificaciones (separadas por coma): ")
    
    alumno = (nombre, edad, calificaciones)
    alumnos.append(alumno)

print("\n--- Lista de Alumnos ---")
for alumno in alumnos:
    print(alumno)