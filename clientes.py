def menu_clientes():
    print("\n", "*" * 10)
    print("\nM E N U C L I E N T E S\n")
    print("1. Ingresar cliente")
    print("2. Consultar cliente") 
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar")
    opcion = int(input("Ingrese una opción: "))
    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_clientes()
    elif opcion == 1:
        id_cliente = int(input("\nIngrese el ID del cliente: "))
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        ingresar_cliente(id_cliente, nombre, direccion, telefono)
        menu_clientes()
    elif opcion == 2:
        consultar_cliente()
        menu_clientes()
    elif opcion == 3:
        modificar_cliente()
        menu_clientes()
    elif opcion == 4:
        eliminar_cliente()
        menu_clientes()


def ingresar_cliente(id_cliente, nombre, direccion, telefono):
    with open("clientes.txt", "a") as archivo:
        archivo.write(f"{id_cliente}-{nombre}-{direccion}-{telefono}\n")


def consultar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))  # Solicita al usuario el ID del cliente
    with open("clientes.txt", "r") as archivo:  # Abre el archivo en modo lectura
        for linea in archivo:  # Itera a través de cada línea del archivo
            datos = linea.strip().split('-')  # Divide la línea por '-' para obtener los datos del cliente
            if datos[0] == str(id_cliente):  # Compara el ID del cliente con el ID ingresado
                # Imprime los detalles del cliente si el ID coincide
                print(f"ID: {datos[0]}, Nombre: {datos[1]}, Dirección: {datos[2]}, Teléfono: {datos[3]}")
                return  # Retorna si se encuentra el cliente
    print("Cliente no encontrado")  # Imprime un mensaje si no se encuentra el cliente


def modificar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))  # Solicita al usuario el ID del cliente
    nombre = input("Ingrese el nuevo nombre del cliente: ")  # Solicita el nuevo nombre
    direccion = input("Ingrese la nueva dirección del cliente: ")  # Solicita la nueva dirección
    telefono = input("Ingrese el nuevo teléfono del cliente: ")  # Solicita el nuevo teléfono

    lines = []
    with open("clientes.txt", "r") as archivo:  # Abre el archivo en modo lectura
        lines = archivo.readlines()  # Lee todas las líneas y las almacena en una lista

    with open("clientes.txt", "w") as archivo:  # Abre el archivo en modo escritura
        for linea in lines:  # Itera a través de cada línea en la lista
            datos = linea.strip().split('-')  # Divide la línea por '-' para obtener los datos del cliente
            if datos[0] == str(id_cliente):  # Compara el ID del cliente con el ID ingresado
                # Si el ID coincide, escribe los nuevos datos en el archivo
                archivo.write(f"{id_cliente}-{nombre}-{direccion}-{telefono}\n")
            else:
                archivo.write(linea)  # Si el ID no coincide, escribe la línea original


def eliminar_cliente():
    id_cliente = int(input("Ingrese el ID del cliente: "))  # Solicita al usuario el ID del cliente

    lines = []
    with open("clientes.txt", "r") as archivo:  # Abre el archivo en modo lectura
        lines = archivo.readlines()  # Lee todas las líneas y las almacena en una lista

    with open("clientes.txt", "w") as archivo:  # Abre el archivo en modo escritura
        for linea in lines:  # Itera a través de cada línea en la lista
            datos = linea.strip().split('-')  # Divide la línea por '-' para obtener los datos del cliente
            if datos[0] != str(id_cliente):  # Compara el ID del cliente con el ID ingresado
                archivo.write(linea)  # Si el ID no coincide, escribe la línea original

    print("Cliente eliminado")  # Imprime un mensaje indicando que el cliente fue eliminado

# Llamar a la función del menú para iniciar
menu_clientes()
