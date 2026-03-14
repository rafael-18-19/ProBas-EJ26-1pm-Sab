texto = input("ingrese una cadena de texto:")

vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("la cantidad de vocales es:", contador)