def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

entrada = input("Ingresa las calificaciones separadas por espacios: ")

lista_calificaciones = [float(nota) for nota in entrada.split()]

promedio = calcular_promedio(lista_calificaciones)
print("El promedio es:", promedio)
