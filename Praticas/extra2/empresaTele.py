
def menu(data):
    while True:
        opcao = 0
        while opcao not in {'1','2','3','4','5'}:
            print("1) Registar chamada")
            print("2) Ler ficheiro")
            print("3) Listar clientes")
            print("4) Fatura")
            print("5) Terminar")
            opcao = input("Opção? ")
        if opcao == '1':
            regCal(data)
        elif opcao == '2':
            lerFil(data)
        elif opcao == '3':
            lisCli(data)
        elif opcao == '4':
            fatCli(data)
        else:
            break

def custoCal(cal):
    if cal[0][0] == cal[1][0] and cal[0][1] == cal[1][1]:
        return 0.04
    elif cal[1][0] == '2':
        return 0.02
    elif cal[1][0] == '+':
        return 0.80
    return 0.10

def fatCli(data):
    num = 0
    total = 0
    while num not in allCli(data):
        num = input("Cliente? ")
    print(data)
    allCal = filter(lambda c: c[0] == num,data)
    print(f"Fatura do cliente {num}")
    print(f"{'Destino':<15}",end='')
    print(f"{'Duração':>10}",end='')
    print(f"{'Custo':>10}")
    for cal in allCal:
        print(f"{cal[1]:<15}",end='')
        print(f"{cal[2]:>10}",end='')
        custo = round(custoCal(cal) * (int(cal[2])/60),2)
        print(f"{custo:>10}")
        total += custo
    print(f"{'Total:':>25}",end='')
    print(f"{total:>10}")


def allCli(data):
    allCli = set()
    for i in data:
        allCli.add(i[0])
    return allCli

def lisCli(data):
    print("Clientes: ",end='')
    for i in allCli(data):
        print(i,end=' ')
    print()
    return allCli


def lerFil(data):
    fileName = input("Ficheiro? ")
    try:
        with open(fileName,'r',encoding='utf-8') as file:
            for line in file:
                line = line.strip().split()
                print(f"{line[0]:<15}",end='')
                print(f"{line[1]:<15}",end='')
                print(f"{line[2]:>5}")
                data.append(line)
    except:
        print(f"\nErro ao abrir o ficheiro - '{fileName}'",end='\n\n')



def regCal(data):
    OriTel = ''
    DesTel = ''
    dur = ''
    while not valTel(OriTel):
        OriTel = input("Telefone origem? ")
    while not valTel(DesTel):
        DesTel = input("Telefone destino? ")
    while not dur.isnumeric():
        dur = input("Duração (s)? ")
    data.append([OriTel,DesTel,dur])


def valTel(tel):
    if (not 2 < len(tel) < 10) or (tel[0] == '+' and (not 3 < len(tel) < 11)):
        return False
    if tel[0] == '+':
        num = tel[1:]
    else:
        num = tel
    if num.isnumeric():
        return True
    else:
        return False

def main():
    data = []
    menu(data)



if __name__ == '__main__':
    main()