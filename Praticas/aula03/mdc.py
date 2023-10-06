def mdc(a,b):
    resto = a%b
    if (resto == 0):
        return b
    else:
        return mdc(a,resto)


a=69
b=30
print(mdc(a,b))