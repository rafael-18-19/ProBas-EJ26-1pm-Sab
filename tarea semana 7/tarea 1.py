def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

entrada = input("ingresa un alista de numeros separados por espacios: ")
numeros = [float(x) for x in entrada.split()]

promedio =calcular_promedio(numeros)
print(f"su promedio es", {promedio})