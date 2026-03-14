n = int(input("Ingresa la posición n: "))

a = 0
b = 1

if n == 1:
    print("El término es:", a)
elif n == 2:
    print("El término es:", b)
else:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print("El término es:", b)
