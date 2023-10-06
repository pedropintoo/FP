# Complete o programa!
from tkinter import filedialog

# a)
def loadFile(fname, lst):
    with open(fname,'r') as file:
        for line in file:
            line = line.strip()
            line = line.split('\t')
            if line[0] != "Numero":
                lst.append((int(line[0]),line[1],int(line[2]),line[3],line[4],float(line[5]),float(line[6]),float(line[7])))         
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    return round((reg[-3] + reg[-2] + reg[-1])/3,1) 


# c) Crie a função printPauta aqui...
def printPauta(lst,file):
    print(f"{'Numero'}{'Nome':^60}{'Nota':4}")
    print(f"{'Numero'}{'Nome':^60}{'Nota':4}",file=file)
    for reg in lst:
        final = notaFinal(reg)
        nome = reg[1]
        print(f'{reg[0]:6}{nome:^60}{final:4}')
        print(f'{reg[0]:6}{nome:^60}{final:4}',file=file)

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile('C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula06\\school1.csv', lst)
    loadFile('C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula06\\school2.csv', lst)
    loadFile('C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula06\\school3.csv', lst)
    
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    file = open(filedialog.askopenfilename(title="Choose File"),"a")
    printPauta(lst,file)
    file.close()


# Call main function
if __name__ == "__main__":
    main()


