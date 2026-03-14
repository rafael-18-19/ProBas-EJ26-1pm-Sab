agenda = {}
while True:
    print("\n1. Agregar contacto | 2. Buscar contacto | 3. Eliminar contacto | 4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")
    elif opcion == '2':
        nombre = input("Ingresa el nombre a buscar: ")
        print(f"Teléfono: {agenda.get(nombre, 'Contacto no encontrado.')}")
    elif opcion == '3':
        nombre = input("Ingresa el nombre a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")
    elif opcion == '4':
        break
    else:
        print("Opción no válida.")