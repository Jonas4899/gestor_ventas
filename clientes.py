from utilidades import *

ARCHIVO = "clientes.txt"

def menu_clientes():
    print(f"\n{" - " * 30}\n")
    print("\nM E N U C L I E N T E S\n")
    print("1. Ingresar cliente")
    print("2. Consultar cliente")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar")
    opcion = int(input("Ingrese una opción: "))
    print(f"\n{" - " * 10}\n")
    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_clientes()
    elif opcion == 1:
        id_cliente = int(input("\nIngrese el ID del cliente: "))
        ingresar_cliente(id_cliente)
        menu_clientes()
    elif opcion == 2:
        general = input("Desea ver la lista de todos los clientes? (s/n): ")
        if general == "s":
            consulta_general_clientes()
        else:
            consultar_cliente()
        menu_clientes()
    elif opcion == 3:
        modificar_cliente()
        menu_clientes()
    elif opcion == 4:
        eliminar_cliente()
        menu_clientes()


def ingresar_cliente(id_cliente):
    clientes_guardados = []
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                clientes_guardados.append(int(datos[0]))
    except:
        print("\nCreando archivo de Clientes...\n")
    finally:
        with open(ARCHIVO, "a") as archivo:
            if id_cliente in clientes_guardados:
                print("\nEl ID del cliente ya existe!")
            else:
                nombre = input("Ingrese el nombre del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                archivo.write(f"{id_cliente}-{nombre}-{direccion}-{telefono}\n")


def consulta_general_clientes():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                print(
                    f"\n• ID: {datos[0]}\n• Nombre: {datos[1]}\n• Dirección: {datos[2]}\n• Teléfono: {datos[3]}\n"
                )


def consultar_cliente():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                if datos[0] == str(id_cliente):
                    print(
                        f"\n• ID: {datos[0]}\n• Nombre: {datos[1]}\n• Dirección: {datos[2]}\n• Teléfono: {datos[3]}"
                    )
                    return
        print("\nCliente no encontrado :(")


def modificar_cliente():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        id_cliente = int(input("Ingrese el ID del cliente: "))

        lines = []
        with open(ARCHIVO, "r") as archivo:
            lines = archivo.readlines()

        print(
            f"\nPara modificar los datos del cliente, llene solo los campos que desea cambiar y deje los demás vacíos.\n"
        )

        with open(ARCHIVO, "w") as archivo:
            for linea in lines:
                datos = linea.strip().split("-")
                if datos[0] == str(id_cliente):
                    nombre = input("Ingrese el nuevo nombre del cliente: ")
                    if nombre == "":
                        nombre = datos[1]

                    direccion = input("Ingrese la nueva dirección del cliente: ")
                    if direccion == "":
                        direccion = datos[2]

                    telefono = input("Ingrese el nuevo teléfono del cliente: ")
                    if telefono == "":
                        telefono = datos[3]

                    archivo.write(f"{id_cliente}-{nombre}-{direccion}-{telefono}\n")
                else:
                    archivo.write(linea)


def eliminar_cliente():
    if not existencia_archivo(ARCHIVO):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        lines = []

        with open(ARCHIVO, "r") as archivo:
            lines = archivo.readlines()

        with open(ARCHIVO, "w") as archivo:
            for linea in lines:
                datos = linea.strip().split("-")
                if datos[0] != str(id_cliente):
                    archivo.write(linea)
                else:
                    opcion = input(
                        f"Seguro que desea eliminar al cliente {datos[1]}? (s/n): "
                    )
                    if opcion == "s":
                        print("Cliente eliminado!")
                    else:
                        archivo.write(linea)
