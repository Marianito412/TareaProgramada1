import wikipedia
import re
import html

wikipedia.set_lang("es")
busqueda = "zorro gris patagónico"
a = wikipedia.page("zorro gris patagónico")
b=re.sub(r"\[\d*\]","",wikipedia.summary("zorro gris patagónico"))
<<<<<<< Updated upstream
b.replace("\u200b","")
=======
b=b.replace("\u200b", "").replace("\n","")
>>>>>>> Stashed changes
lista=["zorro gris patagónico",a.title, a.url,b]

print(lista)

