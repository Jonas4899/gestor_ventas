def existencia_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            return True
    except:
        return False
