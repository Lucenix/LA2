#ideia: como a soma é a mesma para todas as listas, guardar quais os elementos que foram utilizados

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