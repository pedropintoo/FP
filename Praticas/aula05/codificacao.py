def codifica(s):
    """
    Devolve versão codificada na string s.
    """
    r = ''
    for c in s:
        code = ord(c)
        c2 = chr(127 - code)
        r += c2
    return r

def descodidifica(a):
    r = codifica(a)
    return r


hacker = codifica("isto EH MARADO")
print('Codificado: ',hacker)
print('\nDescodificado: ',descodidifica(hacker))
