agenda = []

while True:
    print("\n1. Agregar | 2. Buscar | 3. Eliminar | 4. Salir")
    opcion = input("Opción: ")
    
    if opcion == '1':
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correos_input = input("Correos electrónicos (separados por coma): ")
        correos = [c.strip() for c in correos_input.split(',')]
        
        agenda.append({"nombre": nombre, "telefono": telefono, "correos": correos})
        print("Contacto guardado.")
        
    elif opcion == '2':
        busqueda = input("Nombre a buscar: ")
        encontrado = False
        for contacto in agenda:
            if contacto["nombre"].lower() == busqueda.lower():
                print(f"Info: {contacto}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
            
    elif opcion == '3':
        busqueda = input("Nombre a eliminar: ")
        for i, contacto in enumerate(agenda):
            if contacto["nombre"].lower() == busqueda.lower():
                eliminado = agenda.pop(i)
                print(f"Contacto {eliminado['nombre']} eliminado.")
                break
        else:
            print("Contacto no encontrado.")
            
    elif opcion == '4':
        break
    else:
        print("Opción inválida.")