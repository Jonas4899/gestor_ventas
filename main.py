from proveedores import menu_proveedores


def menu_principal():
    print("\n---------------------------\n")
    print("MENU PRINCIPAL\n")
    print("1. Clientes")
    print("2. Proveedores")
    print("3. Inventarios")
    print("4. Ventas")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion < 1 or opcion > 5:
        print("Opción no válida")
        menu_principal()
    elif opcion == 1:
        pass
    elif opcion == 2:
        menu_proveedores()
        menu_principal()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        exit()


menu_principal()
