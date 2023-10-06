def readJornadas(fileName):
    jornadas = {}
    with open(fileName,'r',encoding='utf-8') as file:
        for line in file:
            line = line.strip().split(",")
            jornadas[int(line[0])] = jornadas.get(int(line[0]),list()) + [[line[1],line[2]]]
    return jornadas


def showJornada(games,jornada):
    g = 1
    data = []
    for i in games:
        while True:
            bet = input(f"{g} {i[0]} vs {i[1]}: ").upper()
            if bet in {"1","2","X","1X","X2","12","1X2"}:
                data.append([g,bet])
                break
            print("Aposta inválida! ")
        g += 1

    with open("jornada"+str(jornada)+".csv",'w',encoding='utf-8') as f:
        for i in data:
            print(f"{i[0]}, {i[1]}",file=f)

    cost = round(- ((1**len(list(filter(lambda s: len(s[1]) == 1,data))))*(2**len(list(filter(lambda s: len(s[1]) == 2,data))))*(3**len(list(filter(lambda s: len(s[1]) == 3,data)))))*0.4,2)

    return cost


def showResults(jornada,saldo):
    with open("jornada"+str(jornada)+".csv",'r',encoding='utf-8') as file:
        bets = {}
        for line in file:
            line = line.strip().split(',')
            bets[int(line[0])] = line[1]
    with open("Jogos.csv",'r',encoding='utf-8') as games:
        i = 1
        a = 1
        results = {}
        for line in games:
            e1, e2, g1, g2 = line.strip().split(',')[1:]
            results[a] = results.get(a,[]) + [[e1,e2,g1,g2]]
            i += 1
            if i == 10:
                i = 1
                a += 1
        g = 1
        certas = 0
        for line in results[jornada]:
            e1, e2, g1, g2 = line

            print(f"{g}",end='')
            print(f"{e1:>20}",end='')
            goals = str(g1)+'-'+str(g2)
            print(f"{goals:^10}",end='')
            print(f"{e2:<20}",end='')
            print(f": {str(bets[g]):<5}",end='')
            if g1 == g2:
                score = "X"
            elif g1 > g2:
                score = "1"
            else:
                score = "2"
            if score in bets[g]:
                certas += 1
                print("(CERTO)")
            else:
                print("(ERRADO)")
            g += 1
        print(f"TEM {certas} CERTAS.",end="")
        if certas == 9:
            print("1º PRÉMIO.")
            saldo += 5000
            print(f"Saldo: {saldo} euro")
        elif certas == 8:
            print("2º PRÉMIO.")
            saldo += 1000
            print(f"Saldo: {saldo} euro")
        elif certas == 7:
            print("3º PRÉMIO.")
            saldo += 100
            print(f"Saldo: {saldo} euro")
        else:
            print("SEM PRÉMIO.")
            print(f"Saldo: {saldo} euro")




def main():
    jornadas = readJornadas('Jornadas.csv')
    i = 0
    saldo = 0
    while True:
        while True:
            jornada = input("Jornada? ")
            try:
                if jornada == "0":
                    i = 1
                    break
                if 1 <= int(jornada) <= len(jornadas):
                    break
            finally:
                jornada = int(jornada)
        if i == 1:
            break
        saldo = showJornada(jornadas[jornada],jornada)
        showResults(jornada,saldo)
    return


if __name__ == "__main__":
    main()