def saludar(nombre, edad=18):
    print(f"Hola {nombre}, tienes {edad} años.")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

if edad == "":
    saludar(nombre)
else:
    saludar(nombre, int(edad))
