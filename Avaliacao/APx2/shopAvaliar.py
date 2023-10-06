# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    count = 0
    with open('produtos.txt') as f:
        lines = f.readlines()
        for line in lines:                                 
            if count != 0:
                line = line.strip()                     # ignore \n
                array = line.split(';')
                produtos.update({array[0]: array[1:]})
            count +=1
        #print(dict)


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    # print(produtos)
    # dicionario = {}
    # for key in dict:
    #print(produtos)
    list = []
    list2 = []
    codigo = '22'
    lista_compras = {}
    list_codes = []
    #print(produtos)
    while codigo != '':
        codigo = input("Code? ")
        inputs = codigo.split()

        try:
            codigo = inputs[0]
            list_codes.append(codigo)
            quantidade = inputs[1]
        except IndexError:
            codigo = inputs[0]
            list_codes.append(codigo)
            quantidade = 1
            pass

        for chave in produtos:
            # print(codigo)
            # print(chave)
            if codigo == chave:
                print(codigo)
                # if codigo in list_codes:
                #     # print(lista_compras[])
                #     modifie = lista_compras[codigo]
                #     modifie[1] = modifie[1] + quantidade
                # else:

                list_codes.append(codigo)

                list = produtos[chave]
                list2.append(list[0])
                list2.append(quantidade)
                list2.append(list[2])
                #print(list2)
                #print(*list2, sep = " ")
                lista_compras.update({codigo:list2})
        print(lista_compras)        
        

                



def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    


def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    lista_compras = {}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        #Acrescente outras opções aqui...
        if op == "F":
            x = int(input("Numero compra? "))
            y = fatura(produtos, compra[x-1])

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])

