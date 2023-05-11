#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto.
#Fecha de creacion: 18/03/2023 4:37pm
#Ultima version:  05/05/2023 8:03pm
#Version: 3.10.6

#Importación de bibliotecas
from os import path
import pickle

#Definición de funciones
def graba(nomArchGrabar, varGuardar):
    """
    Funcionalidad: Graba un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a escribir
    -varGuardar(any): La variable a guardar
    Salidas: NA
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("Grabando archivo: ", nomArchGrabar)
        pickle.dump(varGuardar,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    """
    Funcionalidad: Lee un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a leer
    Salidas: NA
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("Leyendo archivo: ", nomArchLeer)
        lista = pickle.load(f)
        f.close()
        return lista
    except FileNotFoundError:
        print("Archivo no encontrado: ", nomArchLeer)

def guardarTexto(pNombre, pExtension, pContenido):
    """
    Funcionalidad: Guarda un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    -pContenido(str): El texto a guardar en el archivo
    Salidas:NA
    """
    with open(f"{pNombre}{pExtension}", "w", encoding="utf-8") as archivo:
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
    with open(f"{pNombre}{pExtension}", "r", encoding="utf-8") as archivo:
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
