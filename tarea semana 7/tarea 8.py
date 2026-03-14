def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
#2

from temperatura import convertir_celsius_a_fahrenheit as c_a_f
from temperatura import convertir_fahrenheit_a_celsius as f_a_c

if __name__ == "__main__":
    print("--- Menú de Conversión de Temperatura ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    opcion = input("Elige la conversión deseada (1 o 2): ")
    
    if opcion == '1':
        grados_c = float(input("Ingresa los grados Celsius: "))
        resultado = c_a_f(grados_c)
        print(f"{grados_c} °C equivalen a {resultado} °F")
    elif opcion == '2':
        grados_f = float(input("Ingresa los grados Fahrenheit: "))
        resultado = f_a_c(grados_f)
        print(f"{grados_f} °F equivalen a {resultado} °C")
    else:
        print("Opción no válida.")