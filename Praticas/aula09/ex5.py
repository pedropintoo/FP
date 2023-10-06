import bisect
with open("C:\\Users\\pedro\\OneDrive - Universidade de Aveiro\\Universidade\\1ano\\1semestre\\FP\\P\\aula09\\wordlist.txt",encoding="utf-8") as file:
    lst = []
    for line in file:
        lst.append(line.strip().lower())
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter = 'a'
    prefix = ''
    while True:
        letter = input("Letter: ")
        if (not letter) or (len(letter)>1):
            break
        prefix += letter
        print("Prefix --->",prefix)
        left_start = bisect.bisect_left(lst,prefix)
        if letters.index(letter) == len(letters)-1:
            newLetter = 'a'
        else:
            newLetter = letters[letters.index(letter)+1]
        after_start = bisect.bisect_left(lst,prefix[:-1]+newLetter)
        if left_start == after_start:
            print("Prefix not found")
        else:
            for words in lst[left_start:after_start]:
                print("--> ",words)

