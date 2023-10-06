# Pode correr o programa sem argumentos:
#---> python3 shop
# ou passando outros ficheiros de produtos como argumento:
#---> python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname,'r',encoding='utf8') as file:
        # Divide as linhas em listas pelos ';'
        # Começa apenas no index [1] pois já existe esse produto no dicionário de produtos
        line = [line.strip().split(';') for line in file][1:]
        # Atualização dos produtos
        # line[p][0] é o código do produto (eg."p21")
        # Adiciona á key(código) uma tuple como value
        # Essa tuplo tem os vários elementos (nome,secção,preço,iva) sendo o preço e o iva convertidos para float
        produtos.update({line[p][0] : tuple([i if j<2 else (float(i) if j==2 else float(f'{i[:-1]}')/100) for j,i in enumerate(line[p][1:])]) for p in range(len(line))})


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    compra = {}
    while True:
        code = input('Code? ').strip()
        # se code estiver vazio termina
        if not code:
            break
        quantidade = 1
        # Criar uma lista do código introduzido pelo utilizador por espaços
        # Pretendido: [código,quantidade]
        code = code.split()
        # Se apenas tiver: [codigo] vamos adicionar para [codigo,quantidade=1]
        if len(code) == 1:
            code.append('1')

        # code[0] é o código do produto e code[1] é a quantidade
        # produtos.keys() são todos os códigos de produtos
        # Verfica também se a quantidade é inteira positva diferente de 0
        if code[0] in produtos.keys() and len(code) == 2 and code[1].isnumeric() and code[1]!='0': 

            # produtos[code[0]] é uma tupla de (nome,secção,preço,iva)
            # produtos[code[0]][2] é o preço (líquido)
            # produtos[code[0]][3] é o iva
            preco = produtos[code[0]][2] * (1+produtos[code[0]][3])
            quantidade = int(code[1])
            preco *= quantidade
            print(f'{produtos[code[0]][0]} {quantidade} {preco:.2f}')

            # Atualiza o dicionario compra pelo {código:quantidadeTOTAL;....}
            # Essa quantidadeTOTAL é a quantidade de produtos já comprados com esse código
            # mais a quantidade de produtos comprado agora
            # compra.get(code[0],0) irá verificar se esse produto já está na lista de compras
            # se existir soma a quantidade de produtos que já foram comprados aos comprados agora
            # caso não exita ele vai somar 0 á quantidade comprada agora
            compra.update({code[0] : compra.get(code[0],0)+quantidade})
    return compra            
    



def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    numeroCompra = input("Numero compra? ")
    # Verifica se o numero da compra existe
    if numeroCompra in str(compra.keys()):
        numeroCompra = int(numeroCompra)

        # Faz uma lista com todas as seccoes que existem nas compras
        seccoes = [produtos[p][1] for p in compra[numeroCompra].keys()]
        produtosSeccoes = {}
        # para cada seccao ele vai verificar quais os produtos da mesma e adicionar a um dicionario
        for s in seccoes: #seccoes
            # lista temporaria com os produtos de uma seccao
            temp = [p for p in compra[numeroCompra].keys() if s == produtos[p][1]]
            produtosSeccoes[s] = temp
        totalBruto = 0
        totalIVA = 0
        totalLiquido = 0
        # Corre todas seccoes (eg. {seccao2:[p2,p3,p4];seccao2:[p21,p1,p5]})
        for s,p in produtosSeccoes.items():
            print(s)
            
            # Para os produtos nas seccoes
            for i in p:
                qnt = compra[numeroCompra][i]
                nome = produtos[i][0]
                iva = produtos[i][3]
                precoBase = produtos[i][2]
                precoLiquido = precoBase * qnt * (1+iva) 

                totalBruto += precoBase * qnt
                totalIVA += precoBase * qnt * iva
                totalLiquido += precoLiquido

                # Imprimir as quantidades,produtos,iva e preço de uma forma expecífica
                print(f"{qnt:>3} {nome:<30}",end='')
                print(f"({round(iva*100):>2}%)",end='')
                print(f"{f'{precoLiquido:.2f}':>11}")
        # Imprimir o totalBruto, totalIVA e totalLiquido de uma forma expecífica
        print(f"{'Total Bruto:':>39}{f'{totalBruto:.2f}':>11}")
        print(f"{'Total IVA:':>39}{f'{totalIVA:.2f}':>11}")
        print(f"{'Total Liquido:':>39}{f'{totalLiquido:.2f}':>11}")




def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    i = 0
    totalCompras = {}
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos) 

            # Se compra estiver vazia ele ignora     
            if compra:
                # i é o numero da compra
                i += 1
                totalCompras.update({i:compra})
        if op == "F":
            fatura(produtos, totalCompras)
        if op == "S":
            repetir = False

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
