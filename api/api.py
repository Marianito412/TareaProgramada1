import wikipedia
import re
import html

wikipedia.set_lang("es")
busqueda = "Pato de Eaton"
c=wikipedia.search("Pato de Eaton")[0]
a = wikipedia.page(c,auto_suggest=False)
b=re.sub(r"\[\d*\]","",wikipedia.summary(c,auto_suggest=False))
b.replace("\u200b","")
lista=["Pato de Eaton",a.title, a.url,b]

print(lista)

