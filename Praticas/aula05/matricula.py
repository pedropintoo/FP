def matriculaValida(s):
    """Devolve True se s é uma matricula portuguesa da form a AA-88-88"""
    valido = len(s) == 8 and\
             s[2::3] == '--'\
             'A' <= s[0] <= 'Z' and 'A' <= s[1] <= 'Z' and\
             s[3:5].isdigit() and s[6:].isdigit()
    return valido


print(matriculaValida("AA-23-11"))

            
