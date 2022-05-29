#ideia: como a soma é a mesma para todas as listas, guardar quais os elementos que foram utilizados

def valida(soma, lista):
    s = {0}
    for i in range(0, len(lista)):
        d = set()
        for v in s:
            if lista[i] <= soma:
                d.add(lista[i]+v)
        s = s.union(d)
    return soma in s
    
def validas(soma,listas):
    if soma == 0:
        return listas
    return list(filter(lambda lista: valida(soma, lista), listas))

#def rec 80%
def valida(soma, lista):
    if soma == 0:
        return True
    for l in lista:
        tmp = lista.copy()
        tmp.remove(l)
        if valida(soma-l, tmp):
            return True
    return False

def validas(soma,listas):
    lis = list()
    for lista in listas:
        if valida(soma, lista):
            lis.append(lista)
    return lis