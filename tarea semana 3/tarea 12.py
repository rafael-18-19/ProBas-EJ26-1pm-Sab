def encontrar_moda():
    print("--- Cálculo de la Moda ---")
    entrada = input("Ingresa una lista de números separados por espacios: ")
    
    try:
        lista_numeros = [float(x) for x in entrada.split()]
        
        if not lista_numeros:
            print("La lista está vacía.")
            return

        frecuencia = {}
        for numero in lista_numeros:
            if numero in frecuencia:
                frecuencia[numero] += 1
            else:
                frecuencia[numero] = 1
        
        moda = None
        max_frecuencia = 0
        
        for numero, cantidad in frecuencia.items():
            if cantidad > max_frecuencia:
                max_frecuencia = cantidad
                moda = numero
        
        if max_frecuencia == 1 and len(lista_numeros) > 1:
             print("No hay una moda clara (todos los números aparecen 1 vez).")
        else:
             print(f"La moda de la lista es: {moda} (aparece {max_frecuencia} veces)")
             
    except ValueError:
        print("Error: Por favor ingresa solo valores numéricos separados por espacio.")

encontrar_moda()