# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json

# Abre o ficheiro e descodifica-o criando o objeto twits.
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)

# Analise os resultados impressos para perceber a estrutura dos dados.
#print(type(twits))       # deve indicar que é uma lista!
#print(type(twits[0]))    # cada elemento da lista é um dicionário.
#print(twits[0].keys())   # mostra as chaves no primeiro elemento.

# Cada elemento contém uma mensagem associada à chave "text":
#print(twits[0]["text"])
lst = []
for i in twits:
    if i["text"]:
        lst += (i["text"].split())

lst = sorted(lst,key= lambda s: -lst.count(s))
print(lst)
lstHashtags = list(filter(lambda s: s[0] == "#",lst))
max = lstHashtags.count(lstHashtags[0])
prop = 18/max
set = set()
for i in lstHashtags:
    if i in set:
        continue
    else:
        print(f"{i:<35}",end='')
        num = lstHashtags.count(i)
        print(f"{'('+str(num)+')':8>}",end=' ')
        print("+"*int(prop*num))
    set.add(i)

# Algumas mensagens contêm hashtags:
#print(twits[880]["text"])

