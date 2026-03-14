entrada = input("Ingresa una lista de números separados por espacios: ")

numeros = list(map(float, entrada.split()))

mayor = max(numeros)
menor = min(numeros)

print("El número mayor es:", mayor)
print("El número menor es:", menor)
