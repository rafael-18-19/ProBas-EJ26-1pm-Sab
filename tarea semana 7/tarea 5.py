def suma_naturales(n):
    if n <= 0:
        return 0
    return n + suma_naturales(n - 1)

limite = int(input("Ingresa hasta qué número natural deseas sumar (n): "))
print(f"La suma de los primeros {limite} números naturales es: {suma_naturales(limite)}")