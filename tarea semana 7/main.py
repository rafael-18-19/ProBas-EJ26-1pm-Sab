#ejercicio 9
# main.py
from calculadora_cientifica import CalculadoraCientifica

mi_calculadora = CalculadoraCientifica()

raiz = mi_calculadora.calcular_raiz_cuadrada(144)
logaritmo = mi_calculadora.calcular_logaritmo(100, 10)
potencia = mi_calculadora.calcular_potencia(2, 8)
seno = mi_calculadora.calcular_seno(90)

print(f"Raíz cuadrada de 144: {raiz}")
print(f"Logaritmo base 10 de 100: {logaritmo}")
print(f"Potencia de 2^8: {potencia}")
print(f"Seno de 90 grados: {seno}")