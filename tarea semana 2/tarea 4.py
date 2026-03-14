n = int(input("Ingresa un número entre 1 y 50: "))

if n < 1 or n > 50:
    print("Error: El número debe estar entre 1 y 50.")
else:
    a, b = 0, 1
    print("Secuencia de Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
