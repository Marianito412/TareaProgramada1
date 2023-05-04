from os import path

def guardarTexto(pNombre, pExtension, pContenido):
    """
    Funcionalidad: Guarda un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    -pContenido(str): El texto a guardar en el archivo
    Salidas:NA
    """
    with open(f"{pNombre}{pExtension}", "w") as archivo:
        archivo.write(pContenido)

def cargarTexto(pNombre, pExtension):
    """
    Funcionalidad: Lee un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    Salidas:
    -contenido(str): El contenido del archivo
    """
    with open(f"{pNombre}{pExtension}", "r") as archivo:
        contenido=archivo.read()
    return contenido

def esValido(pNombre):
    """
    Funcionalidad: Verifica la validez de un archivo
    Entradas:
    -pNombre(str): El nombre del archivo
    Salidas:
    return(bool): verdadero si pNombre es un archivo válido
    """
    return path.exists(pNombre) and path.isfile(pNombre)
