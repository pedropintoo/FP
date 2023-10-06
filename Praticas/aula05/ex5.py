def countDigits(string):
    total = 0
    for i in string:
        if i.isdigit():
            total+=1
    return total



str = input("? ")
print(countDigits(str))