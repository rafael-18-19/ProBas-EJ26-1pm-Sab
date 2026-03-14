#completar codigo ejer 1:

def generar_fibonacci(n):
    fibonacci = [0, 1]  # Rellenado: [0, 1] Inicializa la lista con 0 y 1
    while len(fibonacci) < n:
        # Se agrega el siguiente elemento a la lista
        fibonacci.append(fibonacci[-1] + fibonacci[-2]) # Rellenado: append
    return fibonacci  # Rellenado: fibonacci (retorna la lista)

resultado = generar_fibonacci(10) # Rellenado: generar_fibonacci (Llamada a la función)
print("Serie de Fibonacci:", resultado)

#ejer 2:
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "") # Rellenado: replace (Reemplaza " " por "")
    cadena = cadena.lower() # Rellenado: lower (Hace todo minúsculas)
    cadena2 = ""
    n = len(cadena)
    
    # El for recorre de forma inversa cadena
    # Rellenado: n - 1, -1, -1 (Inicio, fin, y paso hacia atrás)
    for i in range(n - 1, -1, -1):
        cadena2 += cadena[i] # Rellenado: += (Concatenamos la letra nueva)
        
    return cadena == cadena2 # Rellenado: == (Comparamos si son iguales)

resultado = es_palindromo("Anita lava la tina")
print("¿Es palíndromo?", resultado)

#ejer 3:
def calcular_mediana(lista):
    lista_ordenada = sorted(lista) 
    
    n = len(lista_ordenada) 
    
    if n % 2 == 0: 
        n1 = lista_ordenada[n // 2 - 1] 
        n2 = lista_ordenada[n // 2]     
        mediana = (n1 + n2) / 2
    else:
        mediana = lista_ordenada[n // 2]
        
    return mediana

numeros = [4, 2, 9, 1, 5, 6]
resultado = calcular_mediana(numeros)
print("La mediana es:", resultado)