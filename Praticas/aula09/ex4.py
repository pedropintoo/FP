import bisect
with open("C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula09\\wordlist.txt",encoding="utf-8") as file:
    lst = []
    for line in file:
        lst.append(line.strip().lower())
    ea_start = bisect.bisect_left(lst, "ea")
    eb_start = bisect.bisect_left(lst, "eb")
    ea_count = eb_start - ea_start
    print("'ea' times --> ",ea_count)

    truo_start = bisect.bisect_left(lst, "truo")
    trup_start = bisect.bisect_left(lst, "trup")
    truo_count = trup_start - truo_start
    if truo_count:
        print("'truo' times --> ",truo_count)
    else:
        print("'truo' not found")
        print(bisect.bisect_left(lst, "b"))
        print(bisect.bisect_right(lst, "b"))
        print("A letra maior que 'o' depois de um 'tru' é ---> ",lst[trup_start][3])
