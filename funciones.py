import random
import wikipedia
<<<<<<< Updated upstream

=======
import archivos
import re
from bs4 import BeautifulSoup
>>>>>>> Stashed changes

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

def crearExpediente(pLista,opcion):
    wikipedia.set_lang("es")
<<<<<<< Updated upstream
    for i in pLista:
        busqueda = i
        a = wikipedia.summary(wikipedia.search(busqueda)[0])
        print(a)
        print("------------------")
        print(" ")
    
=======
    busqueda = pLista[opcion]
    print(busqueda)
    a = wikipedia.page(busqueda)
    b=re.sub(r"\[\d*\]","",wikipedia.summary(busqueda))
    b=b.replace("\u200b", "").replace("\n","")
    lista=[pLista[opcion],a.title, a.url,b]
    pLista[opcion]=lista
    return pLista
>>>>>>> Stashed changes

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

    
