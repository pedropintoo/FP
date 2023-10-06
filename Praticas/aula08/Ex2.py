

def main():
    with open('C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula08\\names.txt','r',encoding='utf8') as file:
        lst = [line.strip().split() for line in file][1:]
    
    d = {name[-1]:{i[0] for i in lst 
                        if i[-1]==name[-1]} for name in lst}

    for a in d.items():
        print(a)
        


if __name__ == '__main__':
    main()