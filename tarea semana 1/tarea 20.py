def determinar_tipo_triangulo():
    print("--- Clasificador de Triángulos ---")
    
    try:
        lado_a = float(input("Ingresa la longitud del primer lado: "))
        lado_b = float(input("Ingresa la longitud del segundo lado: "))
        lado_c = float(input("Ingresa la longitud del tercer lado: "))
        
        if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
            print("\nError: Las longitudes deben ser números mayores a 0.")
            return

        if (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
            print("\nEsas medidas no pueden formar un triángulo válido.")
            return

        if lado_a == lado_b == lado_c:
            print("\nEl triángulo es: EQUILÁTERO (todos sus lados son iguales).")
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("\nEl triángulo es: ISÓSCELES (tiene exactamente dos lados iguales).")
        else:
            print("\nEl triángulo es: ESCALENO (todos sus lados son diferentes).")
            
    except ValueError:
        print("\nError: Por favor, ingresa únicamente valores numéricos.")

determinar_tipo_triangulo()