from traceback import print_tb
from utilidades import existencia_archivo

CLIENTES = "clientes.txt"
ARTICULOS = "articulos.txt"

def menu_ventas():
    print("\n"," - "*25)
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
        menu_ventas()
    elif (opcion == 1):
        
        print("\nRegistrar venta")
        registrar_venta()
        menu_ventas()
        
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
    
def registrar_venta():
    
    id_cliente = int(input("Digite el ID del cliente: ")) 
    
    if not existencia_archivo(CLIENTES):
        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
    else:
        cliente_registrado = False
        with open(CLIENTES,"r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                
                if datos[0] == str(id_cliente):
                    print("Cliente registrado")
                    cliente_registrado = True
                    
                    id_producto = int(input("Digite el ID del producto: "))
                    
                    if not existencia_archivo(CLIENTES):
                        print("El archivo de Clientes aun no existe! Registre un cliente primero.")
                    
                    else:
                        producto_registrado = False
                        with open(ARTICULOS,"r") as archivo:
                            for linea in archivo:
                                datos = linea.strip().split("-")
                                
                                if datos[0] == str(id_producto):
                                    print("Producto registrado")
                                    producto_registrado = True
                                    
                                    cantidad = int(input("Digite la cantidad del producto"))
                                        
                                    break
                                    
                            if not producto_registrado:
                                print("Producto NO registrado")
                    break
                    
            
            if not cliente_registrado:
                print("Cliente NO registrado")
                    
                         

menu_ventas() #ELIMINAR ESTO AL TERMINAR


    
    
    