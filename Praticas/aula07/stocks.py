
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile('C://Users//pedro//OneDrive - Universidade de Aveiro//Universidade//1ano//1semestre//FP//P//aula07//nasdaq.csv')
    # Show just first and last tuples:
    print("first:", lst[0])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@12:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for i in range(len(lst)):
        name = lst[i][NAME]
        totVol[name] = totVol.get(name,0) + lst[i][VOLUME]

    return totVol

def maxValorization(lst):
    vMax = {}
    for i in range(len(lst)):
        name = lst[i][NAME]
        data = lst[i][DATE]
        vAbertura = lst[i][OPEN]
        vFecho = lst[i][CLOSE]
        valorizacao = round((vFecho/vAbertura - 1) * 100,2)
        if vMax.get(data,0) != 0:
            if valorizacao > vMax[data][1]:
                vMax[data] = (name,valorizacao)
        else:
            vMax[data] = (name,valorizacao)
    return vMax

def stocksByDateByName(lst):
    dic = {}
    ## {date: name: informacao}
    for i in range(len(lst)):
        name = lst[i][NAME]
        data = lst[i][DATE]
        vAbertura = lst[i][OPEN]
        vMax = lst[i][MAX]
        vMin = lst[i][MIN]
        vFecho = lst[i][CLOSE]
        nomeInformacao = {name:(vAbertura,vMax,vMin,vFecho)}
        if dic.get(data,0) == 0: dic[data] = nomeInformacao
        else: dic[data].update(nomeInformacao)


    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for name in portfolio.keys():
        val = portfolio[name] * stocks[date][name][-1]


    return val

if __name__ == "__main__":
    main()
