import random
import wikipedia


def agregarAnimales(pLista,pNumero):
    animales=random.choices(pLista,k=pNumero)
    while len(set(animales))<pNumero:
        cuenta=0
        i=0
        while i<=pNumero-1:
            if animales.count(animales[i])==1:
                i+=1
            else:
                animales.remove(animales[i])
                animales.append(random.choices(pLista,k=1)[0])
                i=0
    print(animales)
    return animales

def crearExpediente(pLista):
    wikipedia.set_lang("es")
    for i in pLista:
        busqueda = i
        a = wikipedia.summary(wikipedia.search(busqueda)[0])
        print(a)
        print("------------------")
        print(" ")
    

def registrarAnotacion(pAnimal, pAnotacion):
    """
    Funcionalidad: Registra una nueva anotación en un animal específico
    Entradas:
    -pAnimal(list): El animal a modificar
    -pAnotacion(str): La anotación a agregar
    Salidas:
    -pAnimal(list): El animal modificado
    """
    pAnimal[-1].append(pAnotacion)
    return pAnimal

    
