#def dynamic
def crescenteDynamic(lista):
    if len(lista) == 0:
        return 0
    dic = {len(lista)-1:1}
    i = len(lista)-2
    while i>=0:
        dic[i] = 1
        mx = 0
        for j in range(i+1, len(lista)):
            if (lista[i]<=lista[j] and dic[j]>mx):
                mx = dic[j]
        dic[i] += mx
        i-=1
    return max(dic.values())


#def memo(incompleta) -> 60%
def crescenteMemo(lista, o, acc):
    if o >= len(lista)-1:
        return 1
    elif o in acc:
        return acc[o]
    else:
        i = o+1
        while i<len(lista):
            if lista[o] <= lista[i]:
                return crescenteMemo(lista,i,acc) + 1
            i+=1
        
def crescente2(lista):
    acc = {}
    for i in range(0,len(lista)):
        acc[i] = crescenteMemo(lista, i, acc)
    return max(acc.values())

#def recursiva(incompleta) -> 60%
def crescenteRec(lista, o):
    if o >= len(lista)-1:
        return 1
    elif lista[o] <= lista[o+1]:
        return crescenteRec(lista, o+1) + 1
    else:
        return crescenteRec(lista, o+1)
        

def crescente1(lista):
    mx = crescenteRec(lista, 0)
    for i in range(1,len(lista)):
        mx = max(mx, crescenteRec(lista, i))
    return mx