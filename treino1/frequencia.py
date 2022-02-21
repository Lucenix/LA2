def frequencia(texto):
    lista = texto.split()
    dic = {}
    for palavra in lista:
        if palavra not in dic:
            dic[palavra] = 0
        dic[palavra] += 1
    return sorted(sorted(dic), key = lambda n: dic[n], reverse = True) #ordenar uma lista ordenada pelas chaves a partir dos valores (em reverso)