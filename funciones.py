import random
import wikipedia
import archivos

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

def crearTag(pEtiqueta, pContenido, pAtributo=""):
    """
    Funcionalidad: Crea un string con formato xml válido
    Entradas:
    -pEtiqueta(str): El nombre de la etiqueta XML
    -pContenido(str): El contenido de esa etiqueta
    -pAtributo(str): Cualquier atributo deseado
    """
    return f"<{pEtiqueta} {pAtributo}>\n\t{pContenido}\n</{pEtiqueta}>"

def generarXML(pAnimales):
    xml = ""
    for animal in pAnimales:
        infoAnimal = ""
        atributos = ["Nombre", "Título", "URL", "Resumen"]
        for atributo, valor in zip(atributos, animal):
            infoAnimal+=crearTag(atributo, valor)
        xml += crearTag("Animal", infoAnimal, pAtributo=f"Nombre = '{animal[0]}'")
    return xml
        
if __name__=="__main__":
    print(crearTag("book", crearTag("title", "Cool", pAtributo="isbn ='123123'")+"\n"+crearTag("author", "Me")))

archivos.guardarXML("test2", generarXML([["Oso Polar", "Titulo", "URL", "Resumen", []], ["Jirafa Reticulada", "Titulo", "URL","Resumen", []]]))
