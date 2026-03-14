L1 = input("introduce la 1ra lista de numeros ordenados (separados por espacio): ")
L2 = input("introduce la 2da lista de numeros ordenados (separados por espacio): ")

lista1 = [int(x) for x in L1.split()]
lista2 = [int(x) for x in L2.split()]

lista_fusionada = sorted(lista1 + lista2)
print(f"lista fusionada y ordenada: {lista_fusionada}")