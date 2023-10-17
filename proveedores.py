def menu_proveedores():
    print("\n", "*" * 10)
    print("\nMENU PROVEEDORES\n")
    print("1. Ingresar artículo")
    print("2. Consultar artículo")
    print("3. Modificar artículo")
    print("4. Eliminar artículo")
    print("5. Regresar")
    opcion = int(input("Ingrese una opción: "))
    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_proveedores()
    elif opcion == 1:
        codigo = int(input("\nIngresa el codigo: "))
        nombre = input("Ingresa el nombre del producto: ")
        precio = int(input("Ingresa el precio: "))
        ingresar_articulo(codigo, nombre, precio)
        menu_proveedores()
    elif opcion == 2:
        consultar_articulo()
        menu_proveedores()
    elif opcion == 3:
        modificar_articulo()
        menu_proveedores()
    elif opcion == 4:
        eliminar_articulo()
        menu_proveedores()


def ingresar_articulo(codigo, nombre, precio):
    with open("articulos.txt", "a") as archivo:
        archivo.write(f"{codigo}-{nombre}-{precio}\n")


def consultar_articulo():
    codigo = int(input("Ingresa el codigo: "))
    with open("articulos.txt", "r") as archivo:
        pass
    print("Artículo no encontrado")


def modificar_articulo():
    codigo = int(input("Ingresa el codigo: "))
    nombre = input("Ingresa el nuevo nombre del producto: ")
    precio = int(input("Ingresa el nuevo precio: "))

    lines = []
    with open("articulos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("articulos.txt", "w") as archivo:
        for linea in lines:
            datos = linea.strip().split("-")
            if datos[0] == str(codigo):
                archivo.write(f"{codigo}-{nombre}-{precio}\n")


def eliminar_articulo():
    codigo = int(input("Ingresa el codigo: "))
    lines = []
    with open("articulos.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("articulos.txt", "w") as archivo:
        for linea in lines:
            datos = linea.strip().split("-")
            if datos[0] != str(codigo):
                archivo.write(linea)
