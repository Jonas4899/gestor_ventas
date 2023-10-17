def menu_ventas():
    
    print("\n","-"*25)
    print("\n\tMENU VENTAS\n")
    print("1. Registrar venta")
    print("2. Consultar venta")
    print("3. Historial de ventas")
    print("4. Modificar venta")
    print("5. Eliminar venta")
    print("6. Regresar")
    
    opcion = int(input("Digite una opcion: "))
    if opcion < 1 or opcion > 6:
        print("OPCION INVALIDA") 
    elif (opcion == 1):
        print("\nRegistrar venta")
    elif (opcion==2):
        print("\nConsultar venta")
    elif(opcion==3):
        print("\nHistorial ventas")
    elif(opcion==4):
        print("\nmodificar venta")
    elif(opcion==5):
        print("\neliminar venta")
    elif(opcion==6):
        pass
    
            



    
    
    