def maxsoma(lista):
    mx = lista[0]
    last = lista[0]
    for i in range(1, len(lista)):
        if last > 0:
            last += lista[i]
        else:
            last = lista[i]
        mx = max(last,max)
    return mx