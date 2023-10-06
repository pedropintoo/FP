def ispalindrome(string):
    L1 = []
    for i in string:
        if (not i.isspace()):
            L1.append(i.lower())
    L2 = L1.copy()
    L2.reverse()
    return L1 == L2


str = input("? ")
print(ispalindrome(str))