import math


def findZero(func, a, b, tol):

    fa = func(a)
    fb = func(b)
    c = (a+b)/2
    fc = func(c)
    assert fa * fb < 0

    if (b-a)>tol:
        if fc * fa < 0:
            findZero(func, a, c, tol)
        else:
            findZero(func, c, b, tol)
    else:
        print(f"O zero está entre [{a:.5f},{b:.5f}]")


def main():
    f = lambda x: x + math.sin(10*x)
    findZero(f, 0.2, 0.4, 0.0001)

if __name__ == '__main__':
    main()

