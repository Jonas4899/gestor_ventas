from proveedores import menu_proveedores
from clientes import menu_clientes
from ventas import menu_ventas

def menu_principal():
    print(f"\n{" - " * 30}\n")
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
        menu_clientes()
        print("Hola")
        menu_principal()
    elif opcion == 2:
        menu_proveedores()
        menu_principal()
    elif opcion == 3:
        pass
    elif opcion == 4:
        menu_ventas()
        menu_principal()
    elif opcion == 5:
        exit()
        
menu_principal()
