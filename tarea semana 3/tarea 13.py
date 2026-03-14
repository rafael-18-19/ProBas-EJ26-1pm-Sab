def verificar_bisiesto():
    print("--- Verificación de Año Bisiesto ---")
    try:
        entrada = input("Introduce un año para verificar: ")
        anio = int(entrada)
        
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"El año {anio} SÍ es bisiesto.")
        else:
            print(f"El año {anio} NO es bisiesto.")
            
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")

verificar_bisiesto()