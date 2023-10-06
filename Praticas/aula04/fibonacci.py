def fibonacci(n,n1,n2):
    while n > 2:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        n-=1
    print(n3)

n = int(input("n? "))
fibonacci(n,0,1)
