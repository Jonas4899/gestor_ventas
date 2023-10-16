def menu_inventario():
    print("\n", "*" * 10)
    print("\nM E N U I N V E N T A R I O\n")
    print("1. Ingresar artículo")
    print("2. Consultar artículo") 
    print("3. Modificar artículo")
    print("4. Eliminar artículo")
    print("5. Regresar")
    opcion = int(input("Ingrese una opción: "))
    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_inventario()
    elif opcion == 1:
        id_articulo = int(input("\nIngrese el ID del artículo: "))
        nombre = input("Ingrese el nombre del artículo: ")
        cantidad = int(input("Ingrese la cantidad del artículo: "))
        precio_unidad = float(input("Ingrese el precio por unidad del artículo: "))
        ingresar_articulo(id_articulo, nombre, cantidad, precio_unidad)
        menu_inventario()
    elif opcion == 2:
        consultar_articulo()
        menu_inventario()
    elif opcion == 3:
        modificar_articulo()
        menu_inventario()
    elif opcion == 4:
        eliminar_articulo()
        menu_inventario()

def ingresar_articulo(id_articulo, nombre, cantidad, precio_unidad):
    precio_total = cantidad * precio_unidad  # Calcula el precio total
    with open("inventario.txt", "a") as archivo:
        # Incluye el precio total en la información guardada en el archivo
        archivo.write(f"{id_articulo}-{nombre}-{cantidad}-{precio_unidad}-{precio_total}\n")

def consultar_articulo():
    id_articulo = int(input("Ingrese el ID del artículo: "))
    with open("inventario.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split('-')
            if datos[0] == str(id_articulo):
                print(f"ID: {datos[0]}, Nombre: {datos[1]}, Cantidad: {datos[2]}, Precio por Unidad: {datos[3]}, Precio Total: {datos[4]}")
                return
    print("Artículo no encontrado")

def modificar_articulo():
    id_articulo = int(input("Ingrese el ID del artículo: "))
    nombre = input("Ingrese el nuevo nombre del artículo: ")
    cantidad = int(input("Ingrese la nueva cantidad del artículo: "))
    precio_unidad = float(input("Ingrese el nuevo precio por unidad del artículo: "))
    precio_total = cantidad * precio_unidad  # Calcula el precio total
    
    lines = []
    with open("inventario.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inventario.txt", "w") as archivo:
        for linea in lines:
            datos = linea.strip().split('-')
            if datos[0] == str(id_articulo):
                # Incluye el precio total en la información guardada en el archivo
                archivo.write(f"{id_articulo}-{nombre}-{cantidad}-{precio_unidad}-{precio_total}\n")
            else:
                archivo.write(linea)

def eliminar_articulo():
    id_articulo = int(input("Ingrese el ID del artículo: "))

    lines = []
    with open("inventario.txt", "r") as archivo:
        lines = archivo.readlines()

    with open("inventario.txt", "w") as archivo:
        for linea in lines:
            datos = linea.strip().split('-')
            if datos[0] != str(id_articulo):
                archivo.write(linea)

    print("Artículo eliminado")

# Llamar a la función del menú para iniciar
menu_inventario()