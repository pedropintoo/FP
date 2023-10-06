def fat(n):
    return 1 if n <= 1 else n*fat(n-1)


def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n-1) + fibonacci(n-2)


def invert(string):
    return string if len(string) <= 1 else string[-1] + invert(string[:-1])


def som(lst):
    return lst[0] if len(lst) <= 1 else lst[0] + som(lst[1:])


def bigger(lst,big=0):
    if not lst:
        return 0
    return bigger(lst[1:], big=lst[0]) if lst[0] > big else bigger(lst[1:], big=big)


def superLen(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return superLen(lst[0]) + superLen(lst[1:])
    else:
        return 1 + superLen(lst[1:])


print(fat(10))
print(fibonacci(10))
print(invert("morango"))
print(som([1,2,3,4,5,6]))
print(bigger([1,20,3,4,5,7]))
print(superLen([1,2,3,[1,2,3],4,5,[2,[1,2]]]))