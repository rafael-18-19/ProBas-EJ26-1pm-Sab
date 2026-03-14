entrada = input("ingresa una lista de numeros separada por espasios:")

numeros = list(map(float, entrada.split()))

numeros.sort()

print("la lista ordenada de menor a mayor:",numeros)
