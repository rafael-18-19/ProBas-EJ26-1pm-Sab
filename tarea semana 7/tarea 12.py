from cifrador_cesar import CifradorCesar

cifrador = CifradorCesar(3)

mensaje_original = "Hola Mundo 123!"

mensaje_cifrado = cifrador.cifrar(mensaje_original)
print(f"Mensaje cifrado: {mensaje_cifrado}")

mensaje_descifrado = cifrador.descifrar(mensaje_cifrado)
print(f"Mensaje descifrado: {mensaje_descifrado}")