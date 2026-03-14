precios = {}
while True:
    producto = input("Ingresa el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == 'fin':
        break
    precio = float(input(f"Precio de '{producto}': $"))
    precios[producto] = precio

buscar = input("\nIngresa el nombre del producto para consultar su precio: ")
if buscar in precios:
    print(f"El precio de {buscar} es: ${precios[buscar]:.2f}")
else:
    print("Producto no registrado.")