def calculadora_polinomios():
    print("--- Calculadora de Polinomios ---")
    print("Ejemplo: Para 2x^2 + 3x + 1, ingresa: 2 3 1")
    
    try:
        entrada_coefs = input("Ingresa los coeficientes separados por espacio: ")
        coeficientes = [float(x) for x in entrada_coefs.split()]
        
        entrada_x = input("Ingresa el valor de x a evaluar: ")
        x = float(entrada_x)
        
        resultado = 0
        grado = len(coeficientes) - 1
        
        for coef in coeficientes:
            resultado += coef * (x ** grado)
            grado -= 1
            
        print(f"El resultado del polinomio evaluado en x={x} es: {resultado}")
        
    except ValueError:
        print("Error: Asegúrate de ingresar solo números.")

calculadora_polinomios()