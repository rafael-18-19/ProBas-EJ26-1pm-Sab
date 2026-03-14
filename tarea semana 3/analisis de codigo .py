import random

def generar_numeros_aleatorios(n):
    lista = list()
    for i in range(n):
        lista.append(random.randint(1, 100))
        return lista
    resultado = generar_numeros_aleatorios(10)
    print("numeros aleatorios:",resultado)


#pregunta 1
#respuesta = c) crear una lista de numeros aleatorios de longitud n
#pregunta 2
#respuesta = a) es posible que genere numeros repetidos en la lista
#pregunta 3
#respuesta = c) una lista de numeros enteros 
#pregunta 4
#respuesta = a) una lista vacia 
#pregunta 5
#respuesta = c) numeros aleatorios entre 1 y 100


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calcular_mcm(a, b):
    return(a * b) // gcd(a, b)

#ejemplo de uso 
numero1 = int(input("ingresa un numero:"))
numero2 = int(input("ingresa un numero:"))
mcm_resultante = calcular_mcm(numero1, numero2)
print(f"el mcm de {numero1} y {numero2} es: {mcm_resultante}")

#pregunta 1
#respuesta = d) calcular el maximo comun divisor en dos numeros 
#pregunta 2
#respuesta = a)se utiliza para dividir el producto de los numeros 
#pregunta 3
#respuesta = c) 24
#pregunta 4
#respuesta = b) x=10, y=5
#pregunta 5
#respuesta = d) el mcm se calcularia como si numero fuera positivo 
