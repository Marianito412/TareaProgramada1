import random
import wikipedia
import archivos
import re
from os import system

def agregarAnimales(pLista,pNumero):
    """
    Funcionalidad: Esta función agrega una cantidad específica de animales a partir de la lista de animales dada.
    Entradas:
    -pLista(list): Una lista que contiene los animales disponibles para seleccionar.
    -pNumero(int): Un entero que indica la cantidad de animales que se deben agregar.
    Salidas:
    -animales: Una lista que contiene los animales seleccionados y agregados.
    """
    animales=random.choices(pLista,k=pNumero)
    while len(set(animales))<pNumero:
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
    """
    Funcionalidad: Crea un expediente para un animal específico del zoológico.
    Entradas:
    -pLista(list): Una lista que contiene los animales para los cuales se va a crear el expediente.
    -opcion(int): Un entero que indica la posición del animal en la lista "pLista" para el cual se va a crear el expediente.
    Salidas:
    -listaAnimal: El expediente del animal seleccionado.
    -pLista: La lista actualizada con la información del expediente.
    """
    wikipedia.set_lang("es")
    busqueda=wikipedia.search(pLista[opcion])[0]
    a = wikipedia.page(busqueda,auto_suggest=False)
    b=re.sub(r"\[\d*\]","",a.summary)
    b=b.replace("\u200b", "").replace("\n","")
    anotaciones=[]
    listaAnimal=[pLista[opcion],a.title, a.url,b,anotaciones]
    system(f"start chrome {a.images[0]}")
    pLista[opcion]=listaAnimal

    return listaAnimal,pLista

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

def apartarAnimal(pAnimales,pCapacidad):
    """
    Funcionalidad: Apartar una cantidad específica de animales del zoológico
    Entradas:
    -pAnimales(list): Una lista que contiene los animales disponibles para seleccionar.
    -pCapacidad(int): La cantidad de animales que se deben apartar.
    Salidas:
    -animalesTotales(list): Una lista que contiene los animales apartados.
    """
    animales=random.choices(pAnimales,k=pCapacidad)
    animalesTotales=[]
    while len(animalesTotales)<pCapacidad:
        i=0
        while i<=pCapacidad-1:
            if animales.count(animales[i])==1 and animales[i] not in animalesTotales:
                animalesTotales.append(animales[i])
                i+=1
            else:
                animales.remove(animales[i])
                animales.append(random.choices(pAnimales,k=1)[0])
                i=0
    print(animalesTotales)
    return animalesTotales

def crearTag(pEtiqueta, pContenido, pAtributo=""):
    """
    Funcionalidad: Crea un string con formato xml válido
    Entradas:
    -pEtiqueta(str): El nombre de la etiqueta XML
    -pContenido(str): El contenido de esa etiqueta
    -pAtributo(str): Cualquier atributo deseado
    """
    pContenido = pContenido.replace("\n", "\n\t")
    return f"<{pEtiqueta} {pAtributo}>\n\t{pContenido}\n</{pEtiqueta}>"

def generarXML(pAnimales):
    """
    Funcionalidad: Exporta la base de datos a .xml
    Entradas:
    -pAnimales(list): La base de datos a guardar
    Salidas:
    -return(str): El xml generado
    """
    xml = ""
    for animal in pAnimales:
        if isinstance(animal, list):
            infoAnimal = ""
            atributos = ["Nombre", "Titulo", "URL", "Resumen"]
            for atributo, valor in zip(atributos, animal):
                infoAnimal+=crearTag(atributo, valor)+"\n"
            anotaciones=""
            for num, anotacion in enumerate(animal[-1]):
                anotaciones+= crearTag("Anotacion", anotacion, pAtributo=f"indice={num}")+"\n"
            anotaciones = crearTag("Anotaciones", anotaciones)
            infoAnimal+=anotaciones
            xml += crearTag("Animal", infoAnimal, pAtributo=f"Nombre = '{animal[0]}'")+"\n"
        else:
            xml+=crearTag("Animal", animal, pAtributo=f"Nombre = '{animal}'")+"\n"
    return crearTag("Zoologico", xml)

def generarHTML(pAnimales):
    """
    Funcionalidad: Exporta la base de datos a .html
    Entradas:
    -pAnimales(list): La base de datos a guardar
    Salidas:
    -return(str): El html generado
    """
    html=""
    plantilla = archivos.cargarTexto("static/index", ".html")
    for animal in pAnimales:
        if isinstance(animal, list):
            infoAnimal = ""
            for valor in animal[:len(animal)-1]:
                infoAnimal+=crearTag("td", valor)+"\n"
            anotaciones=""
            for num, anotacion in enumerate(animal[-1]):
                anotaciones+= crearTag("Anotacion", anotacion, pAtributo=f"indice={num}")+"\n"
            anotaciones = crearTag("td", anotaciones)
            infoAnimal+=anotaciones
            html += crearTag("tr", infoAnimal, pAtributo=f"Nombre = '{animal[0]}'")+"\n"
        else:
            html+=crearTag("tr",f"<td>{animal}</td><td>Titulo</td><td>URL</td><td>Resumen</td><td>Anotaciones</td>", pAtributo=f"Nombre = '{animal}'")+"\n"
    #html = crearTag("table", html)
    return plantilla.format(test=html)

if __name__=="__main__":
    print(crearTag("book", crearTag("title", "Cool", pAtributo="isbn ='123123'")+"\n"+crearTag("author", "Me")))
    archivos.guardarTexto("test2", ".xml", generarXML([["Oso Polar", "Titulo", "URL", "Resumen", ["test", "anotacion2"]], ["Jirafa Reticulada", "Titulo", "URL","Resumen", ["anotacion"]]]))

