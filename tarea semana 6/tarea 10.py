dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
registro_semanal = []
suma_temp = 0

for dia in dias:
    temp = float(input(f"Ingresa la temperatura del {dia}: "))
    registro_semanal.append((dia, temp)) 
    suma_temp += temp

promedio = suma_temp / len(dias)

print("\n--- Registro de la Semana ---")
for registro in registro_semanal:
    print(f"{registro[0]}: {registro[1]}°C")
print(f"\nTemperatura promedio de la semana: {promedio:.2f}°C")