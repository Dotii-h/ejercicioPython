#Administracion de Propietarios
#Diccionario idependiente, numero departamento y nombre propietario ORGANIZACION
#REQUISITO consulta de propietarios, actualizacion de informacion, agregar departamentos, eliminar registros, mostrar datos.
#Diccionarios
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
edificio = {
    1: piso1,
    2: piso2,
    3: piso3,
    4: piso4
}

while True:
    print(" ADMINISTRACIÓN DEL EDIFICIO ")
    print("1. Consultar propietario")
    print("2. Agregar departamento")
    print("3. Modificar propietario")
    print("4. Eliminar departamento")
    print("5. Mostrar todos los registros")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        piso = int(input("Ingrese el piso (1-4): "))
        depto = input("Ingrese el número de departamento: ")

        if depto in edificio[piso]:
            print("Propietario:", edificio[piso][depto])
        else:
            print("Departamento no encontrado.")

    elif opcion == "2":
        piso = int(input("Ingrese el piso (1-4): "))
        depto = input("Número de departamento: ")
        propietario = input("Nombre del propietario: ")

        edificio[piso][depto] = propietario
        print("Departamento agregado correctamente.")
    
    if opcion == "3":
        propietario =  (input("Igrese propietario a editar"))

   