from datetime import datetime

def calcular_dias_entre_fechas():
    print("--- Calculadora de Días entre Fechas ---")
    formato = "%Y-%m-%d"
    
    try:
        str_fecha1 = input("Ingresa la primera fecha (formato YYYY-MM-DD, ej. 2023-10-25): ")
        str_fecha2 = input("Ingresa la segunda fecha (formato YYYY-MM-DD, ej. 2023-11-05): ")
        
        fecha1 = datetime.strptime(str_fecha1, formato)
        fecha2 = datetime.strptime(str_fecha2, formato)
        
        diferencia = abs((fecha2 - fecha1).days)
        
        print(f"\nEl número de días entre las dos fechas es: {diferencia} días.")
        
    except ValueError:
        print("\nError: Asegúrate de ingresar las fechas exactamente en el formato indicado (YYYY-MM-DD).")

calcular_dias_entre_fechas()