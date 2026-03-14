def calcular_factorial():
    
    try:
        entrada = input("Introduce un número entero no negativo: ")
        numero = int(entrada)

        if numero < 0:
            print("El factorial no está definido para números negativos.")
            return

        factorial = 1

        for i in range(1, numero + 1):
            factorial *= i
            
        print(f"El factorial de {numero} es: {factorial}")

    except ValueError:
        print("Por favor, introduce un número entero válido.")

calcular_factorial()