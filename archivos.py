

def guardarXML(pNombre, pContenido):
    with open(f"{pNombre}.xml", "w") as archivo:
        archivo.write(pContenido)

guardarXML(
            "test","<a>asdf</a>")
