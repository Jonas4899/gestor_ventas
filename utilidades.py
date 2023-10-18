def existencia_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            return True
    except:
        return False


def alerta_stock_minimo():
    articulos_guardados = []
    try:
        with open("articulos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split("-")
                articulos_guardados.append(datos)
    except:
        return
    finally:
        stock_limite = 5
        if not existencia_archivo("config_stock_minimo.txt"):
            with open("config_stock_minimo.txt", "w") as archivo:
                archivo.write("5")
        else:
            with open("config_stock_minimo.txt", "r") as archivo:
                stock_limite = int(archivo.readline().strip())

        for articulo in articulos_guardados:
            if int(articulo[3]) < 5:
                print(
                    f"\nEl articulo '{articulo[1]}' tiene un stock menor al minimo establecido\n"
                )
