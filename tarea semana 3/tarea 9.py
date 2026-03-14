def encontrar_segundo_mayor(lista_numeros):
    unicos = list(set(lista_numeros))
    
    if len(unicos) < 2:
        return "No hay suficientes números únicos"
    
    unicos.sort()
    return unicos[-2]

if __name__ == "__main__":
    datos = [10, 20, 20, 4, 45, 99, 99]
    print(f"Lista original: {datos}")
    print(f"El segundo número mayor es: {encontrar_segundo_mayor(datos)}")