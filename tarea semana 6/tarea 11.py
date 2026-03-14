compras = []
total_gastado = 0

while True:
    producto = input("Nombre del producto (o 'fin' para salir): ")
    if producto.lower() == 'fin':
        break
    cantidad = int(input("Cantidad comprada: "))
    precio_unitario = float(input("Precio unitario: $"))
    
    compras.append((producto, cantidad, precio_unitario))
    total_gastado += (cantidad * precio_unitario)

print("\n--- Detalle del Ticket ---")
for compra in compras:
    print(f"{compra[1]}x {compra[0]} a ${compra[2]:.2f} c/u")
print(f"--------------------------")
print(f"Total a pagar: ${total_gastado:.2f}")