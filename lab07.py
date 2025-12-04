estudiantes = []

def agregar_estudiante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    promedio = float(input("Promedio: "))
    estudiante = {"nombre": nombre, "edad": edad, "promedio": promedio}
    estudiantes.append(estudiante)
    print("Estudiante agregado.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    for e in estudiantes:
        print("Nombre:", e["nombre"], " Edad:", e["edad"], " Promedio:", e["promedio"])
    print()

def mejor_promedio():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    mejor = max(estudiantes, key=lambda x: x["promedio"])
    print("Estudiante con mejor promedio:")
    print("Nombre:", mejor["nombre"], " Edad:", mejor["edad"], " Promedio:", mejor["promedio"], "\n")

def buscar_por_nombre():
    nombre = input("Nombre a buscar: ")
    encontrado = False
    for e in estudiantes:
        if e["nombre"].lower() == nombre.lower():
            print("Nombre:", e["nombre"], " Edad:", e["edad"], " Promedio:", e["promedio"], "\n")
            encontrado = True
    if not encontrado:
        print("No encontrado.\n")

def eliminar_por_nombre():
    nombre = input("Nombre a eliminar: ")
    global estudiantes
    nueva_lista = [e for e in estudiantes if e["nombre"].lower() != nombre.lower()]
    if len(nueva_lista) != len(estudiantes):
        estudiantes = nueva_lista
        print("Estudiante eliminado.\n")
    else:
        print("No se encontró el estudiante.\n")

# menu
while True:
    print("MENU:")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        mejor_promedio()
    elif opcion == "4":
        buscar_por_nombre()
    elif opcion == "5":
        eliminar_por_nombre()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")
