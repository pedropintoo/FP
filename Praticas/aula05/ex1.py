def inputFloatList():
    list = []
    while True:
        numero = (input("Num? "))
        try:
            numero = float(numero)
        except ValueError:
            break
        list.append(float(numero))
    min,max = minmax(list)
    med = (min+max)/2

    print('\n'*10,'Min:  ',min,sep='')
    print('Med: ',med)
    print('Max: ', max,'\n')

    countLower(list,med)

    

def countLower(list,med):
    total = 0
    for i in list:
        if i < med:
            print(i)
            total += 1    
    print('Existem',total,'valores menores que',med)
    
def minmax(list):
    min,max = list[0],list[0]
    for i in list[1:]:
        if(i<min): min = i
        if(i>max): max = i
    return min,max


inputFloatList()
