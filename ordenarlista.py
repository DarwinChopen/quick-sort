def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


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


