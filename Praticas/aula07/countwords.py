
dc = {}
with open("C:/Users/pedro/OneDrive - Universidade de Aveiro/Universidade/1ano/1semestre/FP/P/aula07/pg3333.txt") as f:
    for line in f:
        for w in line.split():
            w = w.lower()
            if w in dc:
                dc[w] += 1
            else:
                dc[w] = 1

print(dc)
print(len(dc))
