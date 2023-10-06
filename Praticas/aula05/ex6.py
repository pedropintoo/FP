def shorten(string):
    Short = ''
    for i in string:
        if i.isupper():
            Short += i
    return Short



str = input("? ")
print(shorten(str))