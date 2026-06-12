#Administracion de Propietarios
#Diccionario idependiente, numero departamento y nombre propietario ORGANIZACION
#REQUISITO consulta de propietarios, actualizacion de informacion, agregar departamentos, eliminar registros, mostrar datos.
# Diccionarios por piso

piso1 = {
    "101": "Juan Vélez",
    "102": "María Soto"
}

piso2 = {
    "201": "Pedro Rojas",
    "202": "Ana Díaz"
}

piso3 = {
    "301": "Carlos Pérez",
    "302": "Claudia Torres"
}

piso4 = {
    "401": "José González",
    "402": "Camila Muñoz"
}

while True:
    print("\n--- ADMINISTRACIÓN DE PROPIETARIOS ---")
    print("1. Consultar propietario")
    print("2. Agregar departamento")
    print("3. Modificar propietario")
    print("4. Eliminar departamento")
    print("5. Mostrar todos los registros")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        piso = input("Ingrese el piso (1-4): ")
        depto = input("Ingrese número de departamento: ")
        if piso == "1":
            print("Propietario:", piso1.get(depto, "No existe"))
        elif piso == "2":
            print("Propietario:", piso2.get(depto, "No existe"))
        elif piso == "3":
            print("Propietario:", piso3.get(depto, "No existe"))
        elif piso == "4":
            print("Propietario:", piso4.get(depto, "No existe"))

    elif opcion == "2":
        piso = input("Ingrese el piso (1-4): ")
        depto = input("Número de departamento: ")
        nombre = input("Nombre del propietario: ")

        if piso == "1":
            piso1[depto] = nombre
        elif piso == "2":
            piso2[depto] = nombre
        elif piso == "3":
            piso3[depto] = nombre
        elif piso == "4":
            piso4[depto] = nombre

        print("Departamento agregado.")

    elif opcion == "3":
        piso = input("Ingrese el piso (1-4): ")
        depto = input("Número de departamento: ")
        nuevo_nombre = input("Nuevo propietario: ")

        if piso == "1" and depto in piso1:
            piso1[depto] = nuevo_nombre
        elif piso == "2" and depto in piso2:
            piso2[depto] = nuevo_nombre
        elif piso == "3" and depto in piso3:
            piso3[depto] = nuevo_nombre
        elif piso == "4" and depto in piso4:
            piso4[depto] = nuevo_nombre
        else:
            print("Departamento no encontrado.")

    elif opcion == "4":
        piso = input("Ingrese el piso (1-4): ")
        depto = input("Número de departamento: ")

        if piso == "1" and depto in piso1:
            del piso1[depto]
        elif piso == "2" and depto in piso2:
            del piso2[depto]
        elif piso == "3" and depto in piso3:
            del piso3[depto]
        elif piso == "4" and depto in piso4:
            del piso4[depto]
        else:
            print("Departamento no encontrado.")

    elif opcion == "5":
        print("\nPISO 1:", piso1)
        print("PISO 2:", piso2)
        print("PISO 3:", piso3)
        print("PISO 4:", piso4)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")