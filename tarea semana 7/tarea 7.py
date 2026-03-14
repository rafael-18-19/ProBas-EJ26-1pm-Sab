import math
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

#archivo 2
import circulo

if __name__ == "__main__":
    radio_usuario = float(input("Ingresa el radio del círculo: "))
    area = circulo.calcular_area_circulo(radio_usuario)
    print(f"El área del círculo es: {area}")