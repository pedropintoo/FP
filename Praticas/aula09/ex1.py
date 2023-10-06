
d = dict()
with open("C:/Users/pedro/OneDrive - Universidade de Aveiro/Universidade/1ano/1semestre/FP/P/aula09/wordlist.txt", 'r',
          encoding='utf-8') as file:
    for line in file:
        line.strip()
        for c in line:
            c.lower()
            if c.isalpha():
                d[c] = d.get(c, 0) + 1  # Se não tiver no dicionario entao mete 0 e adiciona 1


sort = lambda data: data[1]

sortedItems = sorted(d.items(), key=sort, reverse=True)

for i in sortedItems:
    print(i)
    
