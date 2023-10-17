from utilidades import *

ARCHIVO = "articulos.txt"


def menu_proveedores():
    print("\n", " - " * 30, "\n")
    print("\nM E N U    P R O V E E D O R E S\n")
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
        ingresar_articulo(codigo)
        menu_proveedores()
    elif opcion == 2:
        menu_consulta_articulos()
        menu_proveedores()
    elif opcion == 3:
        modificar_articulo()
        menu_proveedores()
    elif opcion == 4:
        eliminar_articulo()
        menu_proveedores()


def ingresar_articulo(codigo):
    articulos_guardados = []
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                articulos_guardados.append(datos)
    except:
        print("\nCreando archivo de Articulos...\n")
    finally:
        existente = False
        for articulo in articulos_guardados:
            if int(articulo[0]) == codigo:
                opcion = input(
                    f"El articulo con Codigo '{codigo}' ya existe. Desea agregar stock al articulo '{articulo[1]}'? (s/n): "
                )
                if opcion == "s":
                    existente = True
                    stock = int(
                        input(f"\nCuantas unidades de '{articulo[1]}' desea agregar?: ")
                    )
                    articulo[3] = int(articulo[3]) + stock
                    break
                else:
                    return

        if existente:
            with open(ARCHIVO, "w") as archivo:
                for linea in articulos_guardados:
                    archivo.write(f"{linea[0]}-{linea[1]}-{linea[2]}-{linea[3]}\n")
        else:
            nombre = input("Ingrese el nombre del articulo: ")
            precio = int(input("Ingrese el precio del articulo: "))
            stock = int(input("Cuantas unidades desea agregar del articulo?: "))
            with open("articulos.txt", "a") as archivo:
                archivo.write(f"{codigo}-{nombre}-{precio}-{stock}\n")


def menu_consulta_articulos():
    print("\n===================================")
    print("Menú de Filtros de Artículos")
    print("===================================")
    print("1. Mostar todos los articulos")
    print("2. Filtrar por Código")
    print("3. Filtrar por Rango de Precio")
    print("4. Filtrar por Stock")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))

    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_proveedores()
    elif opcion == 1:
        consulta_general_articulos()
    elif opcion == 2:
        consulta_articulo_codigo()
    elif opcion == 3:
        consulta_articulo_rango()
    elif opcion == 4:
        consulta_articulo_stock()


def consulta_general_articulos():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Articulos aun no existe! Registre un articulo primero.")
    else:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                print(
                    f"\n• ID: {datos[0]}\n• Nombre: {datos[1]}\n• Precio: {datos[2]}\n• Stock: {datos[3]}\n"
                )


def obtener_articulos_guardados():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
        return []
    else:
        lista_articulos = []

        with open(ARCHIVO, "r") as archivo:
            lines = archivo.readlines()
            for linea in lines:
                datos = linea.strip().split("-")
                lista_articulos.append(datos)

        return lista_articulos


def consulta_articulo_codigo():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        lista_articulos = obtener_articulos_guardados()
        codigo = input("\nIngrese el Codigo del articulo: ")

        for articulo in lista_articulos:
            if articulo[0] == codigo:
                print(
                    f"\n• Codigo: {articulo[0]}\n• Nombre: {articulo[1]}\n• Precio: {articulo[2]}\n• Stock: {articulo[3]}"
                )
                break
        else:
            print("\nArticulo no encontrado :(")


def consulta_articulo_rango():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        lista_articulos = obtener_articulos_guardados()
        min = int(input("\nIngrese el precio minimo del rango: "))
        max = int(input("\nIngrese el precio maximo del rango: "))

        for articulo in lista_articulos:
            if min <= int(articulo[2]) <= max:
                print(
                    f"\n• Codigo: {articulo[0]}\n• Nombre: {articulo[1]}\n• Precio: {articulo[2]}\n• Stock: {articulo[3]}"
                )


def consulta_articulo_stock():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        lista_articulos = obtener_articulos_guardados()
        opcion = int(
            input(
                "\n1. Artículos con stock bajo\n2. Artículos sin stock\n3. Artículos con stock alto\nIngrese una opción: "
            )
        )

        if opcion == 1:
            umbral = int(input("\nIngrese el umbral: "))
            for articulo in lista_articulos:
                if int(articulo[3]) < umbral:
                    print(
                        f"\n• Codigo: {articulo[0]}\n• Nombre: {articulo[1]}\n• Precio: {articulo[2]}\n• Stock: {articulo[3]}"
                    )
        elif opcion == 2:
            for articulo in lista_articulos:
                if int(articulo[3]) == 0:
                    print(
                        f"\n• Codigo: {articulo[0]}\n• Nombre: {articulo[1]}\n• Precio: {articulo[2]}\n• Stock: {articulo[3]}"
                    )
        elif opcion == 3:
            umbral = int(input("\nIngrese el umbral: "))
            for articulo in lista_articulos:
                if int(articulo[3]) > umbral:
                    print(
                        f"\n• Codigo: {articulo[0]}\n• Nombre: {articulo[1]}\n• Precio: {articulo[2]}\n• Stock: {articulo[3]}"
                    )


def modificar_articulo():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        codigo_producto = int(input("Ingrese el codigo del producto: "))

        lines = []
        with open(ARCHIVO, "r") as archivo:
            lines = archivo.readlines()

        with open(ARCHIVO, "w") as archivo:
            for linea in lines:
                datos = linea.strip().split("-")
                if datos[0] == str(codigo_producto):
                    print(
                        f"\nPara modificar los datos del articulo, llene solo los campos que desea cambiar y deje los demás vacíos.\n"
                    )
                    nombre = input("Ingrese el nuevo nombre/descripcion del articulo: ")
                    if nombre == "":
                        nombre = datos[1]

                    precio = input("Ingrese el nuevo precio del producto: ")
                    if precio == "":
                        precio = datos[2]

                    stock = datos[3]

                    archivo.write(f"{codigo_producto}-{nombre}-{precio}-{stock}\n")
                else:
                    archivo.write(linea)
    """
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
    """


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
