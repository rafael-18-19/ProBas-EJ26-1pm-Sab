v1_input = input("introduce el 1er vector ( numeros separados por espacio): ")
v2_input = input("introduce el 2do vector ( numeros separados por espacio): ")

v1 = [float(x) for x in v1_input.split()]
v2 = [float(x) for x in v2_input.split()]

if len(v1) != len(v2):
    print("error: los vectores deben tener la misma longitud.")
else:
    producto = sum(x * y for x, y in zip(v1, v2))
    print(f"el producto escalar es: {producto}")