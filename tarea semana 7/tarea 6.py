def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

terminos = int(input("Ingresa cuántos términos de la secuencia de Fibonacci deseas generar: "))

serie_fibonacci = []
for i in range(terminos):
    serie_fibonacci.append(fibonacci(i))

print(f"La secuencia de Fibonacci es: {serie_fibonacci}")