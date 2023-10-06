def readData(fname):
    with open(fname,'r',encoding='utf-8') as file:
        lst = list()
        for line in file:
            t = tuple(line.strip().split(","))
            lst.append(t)
        lst = lst[1:]
    return lst


def byCountry(country, lst):
    all = list(filter(lambda s: s[2] == country, lst))
    for i in all:
        print(f"{i[1]:<30}",end='')
        print(f"{i[0]:<5}",end='')
        print(f"{i[3]:<5}")


def writeByCountry(country, lst, fname):
    all = list(filter(lambda s: s[2] == country, lst))
    with open(fname,'w',encoding='utf-8') as f:
        for i in all:
            print(f"{i[1]:<30}",end='',file=f)
            print(f"{i[0]:<5}",end='',file=f)
            print(f"{i[3]:<5}",file=f)


def todict(lst):
    dct = dict()
    for i in lst:
        if i[2] not in dct: dct[i[2]] = []
        dct[i[2]].append(i[1])

    return dct


def byUpgrade(lst):
    max = ''
    sub = 0
    for i in lst:
        if int(i[4])>sub:
            max = i[1]
            sub = int(i[4])

    return max


def byClub(club, lst):

    byClub = list(filter(lambda s: s[1] == club, lst))
    if len(byClub) == 0:
        print("Club doesn't exist!")
    else:
        print(byClub)


def byRankingCountry(dct, lst):
    rank = []
    for k, v in dct.items():
        sum = 0
        for club in v:
            sum += int(list(filter(lambda s: s[1] == club, lst))[0][0])

        medRank = round(sum/len(v), 2)
        rank.append([k, medRank])
    rank = sorted(rank, key=lambda c: c[1])
    for i in rank:
        print(f"{i[0]:<25} {i[1]}")


def menu():
    while True:
        print("0 - Abandonar o programa")
        print("1 - Todos os clubes (toda a informação de um ficheiro)")
        print("2 - Informação dos Clubes por país")
        print("3 - Informação dos Clubes por país (escreve em um ficheiro)")
        print("4 - Clubes por país")
        print("5 - Clube que mais subiu no ranking")
        print("6 - Informação por clube")
        print("7 - Ranking dos Paises")
        opcao = ''
        while opcao not in {"0","1","2","3","4","5","6","7"}:
            opcao = input("\nOpção: ")
        print()
        opcao = int(opcao)
        if opcao == 0:
            break
        elif opcao == 1:
            print("Exemplo de ficheiro: 'Soccer_Football Clubs Ranking.csv'")
            filename = input("Nome do ficheiro: ")
            lst = readData(filename)
            print(f"{'Ranking':<10}{'Clube':<30}{'País':<30}{'Pontos atuais':<20}{'Diferença Pontos':<20}{'Pontos antigos':<20}{'Mudança':<20}")
            for i in lst:
                print(f"{i[0]:<10}{i[1]:<30}{i[2]:<30}{i[3]:<20}{i[4]:<20}{i[5]:<20}{i[6]:<20}")
        elif opcao == 2:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            country = input("Nome do país: ")
            byCountry(country,lst)
        elif opcao == 3:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            country = input("Nome do país: ")
            filename = input("Nome do ficheiro: ")
            writeByCountry(country,lst,filename)
        elif opcao == 4:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            dct = todict(lst)
            for i in dct.items():
                print(f"{i[0]:<25}",end="")
                print(i[1])
        elif opcao == 5:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            print(f"Clube que mais subiu no ranking --> {byUpgrade(lst)}\n")
        elif opcao == 6:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            clube = input("Nome do clube: ")
            byClub(clube,lst)
        elif opcao == 7:
            lst = readData("Soccer_Football Clubs Ranking.csv")
            dct = todict(lst)
            byRankingCountry(dct,lst)
    print("Até breve!")


def main():
    menu()


if __name__ == "__main__":
    main()

