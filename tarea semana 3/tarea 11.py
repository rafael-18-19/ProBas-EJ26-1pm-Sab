def calcular_determinante():
    print("--- Cálculo de Determinante 3x3 ---")
    print("Deberás ingresar los valores de la matriz fila por fila.")
    
    matriz = []
    
    for i in range(3):
        try:
            fila_str = input(f"Ingresa los 3 números de la Fila {i+1} separados por espacio: ")
            fila = [float(x) for x in fila_str.split()]
            
            if len(fila) != 3:
                print("Error: Debes ingresar exactamente 3 números por fila.")
                return
            matriz.append(fila)
        except ValueError:
            print("Error: Asegúrate de ingresar solo números.")
            return

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    pos = (a * e * i) + (d * h * c) + (g * b * f)
    neg = (c * e * g) + (f * h * a) + (i * b * d)
    determinante = pos - neg

    print(f"\nMatriz ingresada: {matriz}")
    print(f"El determinante es: {determinante}")

calcular_determinante()