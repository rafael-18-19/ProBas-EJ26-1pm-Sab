import random

def generar_lista_aleatoria():
    print("--- Generador de Números Aleatorios ---")
    
    try:
        n = int(input("¿Cuántos números aleatorios deseas generar?: "))
        
        if n <= 0:
            print("Por favor, ingresa un número mayor a 0.")
            return

        lista_aleatoria = [random.randint(1, 100) for _ in range(n)]
        
        print(f"\nAquí tienes tu lista de {n} números:")
        print(lista_aleatoria)
        
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

if __name__ == "__main__":
    generar_lista_aleatoria()