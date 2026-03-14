num = float(input("ingrese su numero:"))
factorial = 1

while num <= 20:
    factorial *= num
    num -= 1

print("su factorial es",factorial)
