entrada = input("ingrese una lista de numeros separados por espacios:")

numeros = list(map(float, entrada.split()))

suma = sum(numeros)

print("la suma total es:",suma)