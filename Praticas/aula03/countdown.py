def countdown(n):
    while n>=0:
        print(n)
        n-=1

def countdown1(n):   ## Outra solução
    for i in range(n,-1,-1):
        print(i)

n=-1
while n<0:
    n = int(input("Contagem decrescente a partir do número positivo: "))

countdown1(n)