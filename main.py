

import funciones
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

def ESRegistrarAnotaciones(animales):
    """
    Funcionalidad: Muestra interfaz para que el usuario pueda registrar anotaciones para un animal
    Entradas:
    -animales(list): Matriz de animales registrados
    Salidas:
    -animales(list): Matriz de animales registrados ahora con la nueva anotación
    """
    while True:
        for indice, animal in enumerate(animales):
            print(f"{indice+1}. {animal[0]}")
        try:
            eleccion = int(input("Escoja en qué animal desea registrar una nueva anotación: "))-1
            anotacion = input(f"Ingrese la nueva anotación para {animales[eleccion][0]}:\n")
            animales[eleccion] = funciones.registrarAnotacion(animales[eleccion], anotacion)
            print("\nAnotaciones Registradas\n")
            for indice, anotacion in enumerate(animales[eleccion][-1]): # Se asume que solo se necesita mostrar las anotaciones del animal relevante (basado en la elección del usuario)
                print(f"{indice+1} {anotacion}")
            if not validarBin(input("Desea registrar una nueva anotación?\n1. Sí\n2. No\nOpción: ")):
                break
        except ValueError:
            print(f"Opción inválida ingrese un número del 1 al {len(animales)}")
        except IndexError:
            print(f"Opción inválida ingrese un número del 1 al {len(animales)}")
    return animales

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
                opciones = [...,ESRegistrarAnotaciones,exit] #Registrar nuevas funcionalidades acá
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
menu([["Oso Polar", "Título", "URL", "Resumen", []], ["Jirafa Reticulada", "Título", "URL","Resumen", []]])
