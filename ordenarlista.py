def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

estudiantes={}
nombres = []
numeros = [6, 3, 9, 2]
resultado = quick_sort(numeros)
print(resultado)

while True:
    print("1. Ingresar")
    print("2. Mostrar")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ingresar")
            cantidad=int(input("Ingrese la cantidad de Estudiantes que sesea ingresar"))
            for i in range(cantidad):
                print(f"Estudiante #: {i+1}")
                nombre = input(f"Ingresa el nombre #{i+1}: ")
                nombres.append(nombre)
        case 2:
            print("Mostrar")
            resultadonombres = quick_sort(nombres)
            for nombre in resultadonombres:
                print(nombre)
        case 3:
            print("Saliendo")
            break
        case _:
            print("Opcion Invalida")


while True:
    print("Actividad 7")
    print("1. Agregar Estudiantes")
    print("2. Mostrar estudiantes y sus cursos")
    print("3. Buscar por Carne")
    print("4. Salir")
    try:
        opcion=int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))
            for i in range(cantidad):
                print(f"\nEstudiante #{i + 1}")
                while True:
                   carnet = input(int("Ingrese el número de carnet: "))
                   if carnet in estudiantes:
                       print("Este carnet ya existe Ingrese otro")
                   else:
                       break
                estudiantes[carnet] = {}
                estudiantes[carnet]["nombre"] = input("Ingrese el nombre: ")
                estudiantes[carnet]["edad"] = int(input("Ingrese la edad: "))
                estudiantes[carnet]["carrera"] = input("Ingrese la carrera: ")
                estudiantes[carnet]["correo"] = input("Ingrese el correo: ")
                estudiantes[carnet]["telefono"] = input("Ingrese el  teléfono: ")
                estudiantes[carnet]["cursos"] = {}

                cantidad_cursos = int(input("¿A cuantos cursos se inscribirá? "))
                for j in range(cantidad_cursos):
                    print(f"\nCurso #{j + 1}")
                    codigo_curso = input("Código del curso: ")
                    nombre_curso = input("Nombre del curso: ")
                    tarea = float(input("Nota de tarea (0 a 100): "))
                    parcial = float(input("Nota de parcial (0 a 100): "))
                    proyecto = float(input("Nota de proyecto (0 a 100): "))

                    estudiantes[carnet]["cursos"][codigo_curso] = {
                        "nombre": nombre_curso,
                        "tarea": tarea,
                        "parcial": parcial,
                        "proyecto": proyecto
                    }
        case 2:
            print("\nLista de estudiantes registrados:")
            carnets=list(estudiantes.keys())
            ordenarDiccionarios=quick_sort(carnets)

            #for carnet, datos in estudiantes.items():
            for carnet in ordenarDiccionarios:
                datos=estudiantes[carnet]
                print(f"\nCarnet: {carnet}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Edad: {datos['edad']}")
                print(f"Carrera: {datos['carrera']}")
                print(f"Correo: {datos['correo']}")
                print(f"Teléfono: {datos['telefono']}")
                print("Cursos:")
                for codigo, curso in datos["cursos"].items():
                    promedio = (curso["tarea"] + curso["parcial"] + curso["proyecto"]) / 3
                    print(f"  - Código: {codigo}")
                    print(f"     Nombre: {curso['nombre']}")
                    print(f"     Tarea: {curso['tarea']}")
                    print(f"     Parcial: {curso['parcial']}")
                    print(f"     Proyecto: {curso['proyecto']}")
                    print(f"     Promedio: {promedio:.2f}")
        case 3:
            print("\nBúsqueda de estudiante")
            buscado = input("Ingrese el número de carnet que desea buscar: ")

            if buscado in estudiantes:
                est = estudiantes[buscado]
                print("\nEstudiante encontrado:")
                print(f"Nombre: {est['nombre']}")
                print(f"Edad: {est['edad']}")
                print(f"Carrera: {est['carrera']}")
                print(f"Correo: {est['correo']}")
                print(f"Teléfono: {est['telefono']}")
                print("Cursos:")
                for codigo, curso in est["cursos"].items():
                    promedio = (curso["tarea"] + curso["parcial"] + curso["proyecto"]) / 3
                    print(f"  - Código: {codigo}")
                    print(f"     Nombre: {curso['nombre']}")
                    print(f"     Tarea: {curso['tarea']}")
                    print(f"     Parcial: {curso['parcial']}")
                    print(f"     Proyecto: {curso['proyecto']}")
                    print(f"     Promedio: {promedio:.2f}")
            else:
                print("Estudiante no encontrado.")

        case 4:
            print("saliendo...")
            break
        case _:
             print("Opcion invalida")





