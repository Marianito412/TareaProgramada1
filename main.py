
#import wikipedia
#wikipedia.set_lang("es")
#busqueda = "Oso panda"
#a = wikipedia.summary(wikipedia.search(busqueda)[0])
#
#print(a)
#url = "https://es.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exsentences=8&exlimit=2&formatversion=2&origin=*&titles=Ailuropoda%20melanoleuca"

def menu(pMatriz):
    """
    Funcionalidad: Muestra menú principal
    Entradas:
    -pMatriz(list): La matriz a analizar
    Salidas:NA
    """
    while True:
        print(
            "\n"
            "1. Crear expediente\n"
            "2. Registrar anotaciones\n"
            "3. Apartar animal\n"
            "4. Exportar base de datos\n"
            "5. Mostrar base de datos"
        )
        
        opcion= input("Ingrese el número de su opción a elegir: ")
        seguir=True
        while seguir:
            try:
                seguir=False
                opcion = int(opcion)
                opciones = [exit] #Registrar nuevas funcionalidades acá
                #print(pMatriz)
                pMatriz = opciones[opcion-1](pMatriz)
            except IndexError:
                print("La opción indicada no es correcta, debe de ser un número del 1 al 5")
                opcion= input("Ingrese su opcion otra vez: ")
                seguir=True
            except ValueError:
                print("La opción indicada no es un número")
                opcion= input("Ingrese su opcion otra vez: ")
                seguir=True
menu([])
