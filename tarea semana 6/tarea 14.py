ventas = []

while True:
    producto = input("Producto vendido (o 'fin' para terminar registro): ")
    if producto.lower() == 'fin':
        break
    mes = input("Mes de la venta: ")
    cantidad = int(input("Cantidad vendida: "))
    
    venta_actual = {
        "producto": producto,
        "mes": mes,
        "cantidad_vendida": cantidad
    }
    ventas.append(venta_actual)

print("\n--- Resumen de Ventas ---")
for v in ventas:
    print(f"En {v['mes']}, se vendieron {v['cantidad_vendida']} unidades de '{v['producto']}'.")