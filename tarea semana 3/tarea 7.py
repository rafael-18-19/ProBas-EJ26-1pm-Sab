def calcular_mediana(lista_numeros):
    lista_numeros.sort()
    
    n = len(lista_numeros)
    mitad = n // 2

    if n % 2 != 0:
        return lista_numeros[mitad]

    else:
        return (lista_numeros[mitad - 1] + lista_numeros[mitad]) / 2

if __name__ == "__main__":
    numeros = [12, 3, 5, 7, 4, 19, 21] 
    print(f"Lista ordenada: {sorted(numeros)}")
    print(f"La mediana es: {calcular_mediana(numeros)}")