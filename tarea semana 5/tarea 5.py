texto = input("ingrese la cadena a cifrar: ")
desplazamiento = int(input("intruce el desplazamiento (numero entero): "))

resultado = ""
for char in texto:
    if char.isalpha():
        ascii_base = ord('a') if char.islower() else ord('A')
        nuevo_char = chr((ord(char) - ascii_base + desplazamiento) % 26 + ascii_base)
    else:
        resultado += char

print(f"texto cifrado: {resultado}")