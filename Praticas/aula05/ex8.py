def evenThenOdd(s):
    l1 = ''
    l2 = ''
    for p,i in enumerate(s):
        if (p%2==0):
            l1+=i
        else:
            l2+=i
    return l1+l2

def removeAdjacentDuplicates(s):
    for i in range(len(s)):
        if i < len(s)-2:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+1:]
    return s


def reapeatNumTimes(n):
    l = []
    for i in range(n+1):
        for j in range(i):
            l.append(i)
    return l

def positionOfFirstLargest(arr):
    max = arr[0]
    imax = 0
    for p,i in enumerate(arr):
        if max<i:
            max = i
            imax = p  
    return imax
