

import wikipedia
#wikipedia.set_lang("es")
#busqueda = "Oso panda"
#try:
#    a = wikipedia.summary(wikipedia.search(busqueda)[0])
#except wikipedia.exceptions.DisambiguationError as f:
#    lista = f.options[0]
#    print(lista)
#    #a = wikipedia.summary(lista)
#a = wikipedia.page("Oso panda")
#print(a.title, a.url, a.images[0])
#

import funciones

def leerArchivo():
    referencia = open("test1.txt","r")
    print("->Imprime todo el archivo...")
    lista = referencia.readlines()
    lista=[elemento.replace("\n", "")for elemento in lista]
    referencia.close()
    return lista


def validarBin(pEntrada):
    """
    Funcionalidad: Valida una respuesta de si o no
    Entradas:
    -pEntrada(str): Texto conteniendo la opción
    Salida:
    return(bool): True si sí, False si no 
    """
    while True:
        try:
            if int(pEntrada) in [1,2]:
                return int(pEntrada) == 1
            else:
                pEntrada = input("Entrada incorrecta se espera un 1 o 2, vuelva a intentar:\n1. Sí\n2. No\nOpción: ")
        except ValueError:
            pEntrada = input("Entrada incorrecta se espera un 1 o 2, vuelva a intentar:\n1. Sí\n2. No\nOpción: ")

def ESAgregarAnimales(pLista):
    pNumero=input("Ingrese la cantidad de animales que desea añadir a su zoologico: ")
    lista=funciones.agregarAnimales(leerArchivo(),int(pNumero))
    return lista

def AUXESCrearExpediente(pOpcion):
    if isinstance(pOpcion,list):
        return True
    return False

def ESCrearExpediente(pLista):
    i=0
    num=1
    while i<len(pLista):
        if isinstance(pLista[i],list):
            print (f"{num}. {pLista[i][0]}")
        else:
            print (f"{num}. {pLista[i]}")
        i+=1
        num+=1
    opcion=input("Ingrese el numero de animal a generar el expediente")
    if AUXESCrearExpediente(pLista[int(opcion)-1]):
        print("El animal seleccionado ya tiene un expediente")
        return pLista
    listaAnimal,pLista=funciones.crearExpediente(pLista,int(opcion)-1)
    print(
            "\n"
            f"Nombre: {listaAnimal[0]} \n"
            f"Nombre cientifico: {listaAnimal[1]}\n"
            f"Datos: {listaAnimal[3]}\n"
            f"Fuente: {listaAnimal[2]}\n"
        )
    return pLista

def ESRegistrarAnotaciones(pAnimales):

    """
    Funcionalidad: Muestra interfaz para que el usuario pueda registrar anotaciones para un animal
    Entradas:
    -animales(list): Matriz de animales registrados
    Salidas:
    -animales(list): Matriz de animales registrados ahora con la nueva anotación
    """
    while True:
        for indice, animal in enumerate(pAnimales):
            print(f"{indice+1}. {animal[0]}")
        try:
            eleccion = int(input("Escoja en qué animal desea registrar una nueva anotación: "))-1
            anotacion = input(f"Ingrese la nueva anotación para {pAnimales[eleccion][0]}:\n")
            pAnimales[eleccion] = funciones.registrarAnotacion(pAnimales[eleccion], anotacion)
            print("\nAnotaciones Registradas\n")
            for indice, anotacion in enumerate(pAnimales[eleccion][-1]): # Se asume que solo se necesita mostrar las anotaciones del animal relevante (basado en la elección del usuario)
                print(f"{indice+1} {anotacion}")
            if not validarBin(input("Desea registrar una nueva anotación?\n1. Sí\n2. No\nOpción: ")):
                break
        except ValueError:
            print(f"Opción inválida ingrese un número del 1 al {len(pAnimales)}")
        except IndexError:
            print(f"Opción inválida ingrese un número del 1 al {len(pAnimales)}")
    return pAnimales

def AUXApartarAnimal(pAnimales,pCantidad):
    while True:
            try:
                if len(pAnimales)>int(pCantidad):
                    return pCantidad
                else:
                    pCantidad=input(f"El zoologico solo tiene {len(pAnimales)} animales por lo que es menor a la capacidad ingresada, vuelvalo a intentar: ")
            except ValueError:
                pCantidad=input("Se espera un numero, vuelva a intentar: ")

def ESApartarAnimal(pAnimales):
    print("si")
    capacidad=input("Ingrese el numero de animales que el zoologico puede contener: ")
    capacidad=AUXApartarAnimal(pAnimales,capacidad)
    verificacion=validarBin(input("Esta seguro de que quiere generar este cambio?:\n1. Sí\n2. No\nOpción: "))
    if verificacion:
        animales=funciones.apartarAnimal(pAnimales,int(capacidad))
        #animales=funciones.apartarAnimal(pAnimales,int(capacidad))
        print("La lista de los animales actualizada es: ")
        i=0
        num=1
        while i<len(animales):
            if isinstance(animales[i],list):
                print (f"{num}. {animales[i][0]}")
            else:
                print (f"{num}. {animales[i]}")
            i+=1
            num+=1
        return animales
    else:
        return pAnimales

def ESExportarDB(pAnimales):
    """
    Funcionalidad: Muestra interfaz para que el usuario pueda registrar anotaciones para un animal
    Entradas:
    -animales(list): Matriz de animales registrados
    Salidas:
    -animales(list): Matriz de animales registrados ahora con la nueva anotación
    """

def menu():
    """
    Funcionalidad: Muestra menú principal
    Entradas:
    -pMatriz(list): La matriz a analizar
    Salidas:NA
    """
    lista=[]
    while True:
        print(
            "\n"
            "1. Agregar animales\n"
            "2. Crear expediente\n"
            "3. Registrar anotaciones\n"
            "4. Apartar animal\n"
            "5. Exportar base de datos\n"
            "6. Mostrar base de datos"
        )
        
        opcion= input("Ingrese el número de su opción a elegir: ")
        seguir=True
        while seguir:
            try:
                seguir=False
                opcion = int(opcion)
                opciones = [ESAgregarAnimales ,ESCrearExpediente, ESRegistrarAnotaciones,ESApartarAnimal, ESExportarDB, exit] #Registrar nuevas funcionalidades acá
                lista = opciones[opcion-1](lista)
                print("hols")
                print(lista)
##            except IndexError:
##                print("inndex")
##                print("La opción indicada no es correcta, debe de ser un número del 1 al 5")
##                opcion= input("Ingrese su opcion otra vez: ")
##                seguir=True
            except ValueError:
                print("La opción indicada no es un número")
                opcion= input("Ingrese su opcion otra vez: ")
                seguir=True
menu()
