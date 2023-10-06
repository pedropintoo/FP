import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)
    return


def findFiles(path, ext, level=0):
    d = path
    l = []

    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path) and path.endswith(ext):
            print(f"{4*level*' '} FILE {fname}")
            l.append(fname)
        elif os.path.isdir(path):
            print(f"{4*level*' '} DIR {fname}")
            l.extend(findFiles(path,ext,level+1))
        else:
            ftype = "?"

    return l


def main():
    print("Testing printDirFiles('.'):")
    printDirFiles(".")

    print("\nTesting findFiles('.', '.py'):")
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    print("\nTesting findFiles('.', '.csv'):")
    lst = findFiles(".", ".csv")
    print(lst)

if __name__ == "__main__":
    main()

