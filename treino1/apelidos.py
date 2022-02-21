def apelidos(nomes):
    return sorted(sorted(nomes), key = lambda n: len(n.split())-1)