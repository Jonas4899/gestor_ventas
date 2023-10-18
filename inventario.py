from proveedores import menu_consulta_articulos

ARCHIVO = "articulos.txt"


def menu_inventarios():
    print(f"\n{" - " * 30}\n")
    print("MENU INVENTARIOS\n")
    print("1. Actualizar stock de un producto")
    print("2. Consultar inventario")
    print("3. Ajustar stock minimo")
    print("4. Regresar")
    opcion = int(input("Ingrese una opción: "))
    if opcion < 1 or opcion > 4:
        print("Opción no válida")
        menu_inventarios()
    elif opcion == 1:
        actualizar_stock()
        menu_inventarios()
    elif opcion == 2:
        consultar_inventario()
        menu_inventarios()
    elif opcion == 3:
        ajustar_stock_minimo()
        menu_inventarios()


def actualizar_stock():
    articulos_guardados = []
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                articulos_guardados.append(datos)
    except:
        print("\nNo existen articulos para actualizar el stock\n")
        return
    finally:
        codigo = int(input("\nIngresa el codigo: "))
        existente = False
        for articulo in articulos_guardados:
            if int(articulo[0]) == codigo:
                existente = True
                stock = int(
                    input(f"\nCuantas unidades de '{articulo[1]}' desea agregar?: ")
                )
                articulo[3] = int(articulo[3]) + stock
                break
        if existente:
            with open(ARCHIVO, "w") as archivo:
                for linea in articulos_guardados:
                    archivo.write(f"{linea[0]}-{linea[1]}-{linea[2]}-{linea[3]}\n")
        else:
            print("\nEl articulo no existe\n")


def consultar_inventario():
    menu_consulta_articulos()


def ajustar_stock_minimo():
    stock_minimo = int(input("\nIngrese el nuevo stock minimo: "))
    with open("config_stock_minimo.txt", "w") as archivo:
        archivo.write(str(stock_minimo))
    print("\nStock minimo actualizado!\n")
