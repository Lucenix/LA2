
def ladraoDyn(capacidade, objectos):
    dic = {0:0}
    resto = {0:objectos}
    for i in range(1, capacidade+1):
        r = 0
        tmp = objectos.copy()
        for obj in objectos:
            if obj[2]<=i and obj in resto[i-obj[2]]:
                if r < obj[1] + dic[i-obj][2]:
                    r = obj[1] + dic[i-obj[2]]
                    tmp = resto[i-obj][2].copy()
                    tmp.remove(obj)
        d[i] = r
        resto[i] = tmp
    return max(d.values())

#def memo
def ladraoMem(capacidade, objectos):
    dic = dict()
    dic[0] = 0
    return ladraoMemo(capacidade, objectos, dic)

def ladraoMemo(capacidade, objectos, dic):
    #usar as capacidades como chaves não funciona bem: é possível chegar a capacidades iguais por objetos diferentes => o valor final é diferente
    #o melhor seria usar os objetos em si como chaves, mas listas não podem ser usadas como chaves
    if capacidade in dic:
        return dic[capacidade]
    r = 0
    newObj = objectos.copy()
    for obj in objectos:
        if obj[2] <= capacidade and obj in newObj:
            tmp = newObj.copy()
            tmp.remove(obj)
            a = obj[1]+ladraoMemo(capacidade-obj[2], tmp, dic)
            if a > r:
                r = a
                newObj.remove(obj)

    dic[capacidade] = r
    return r

#def rec 80%
def ladraoRec(capacidade,objectos):
    if capacidade == 0:
        return 0
    r = 0
    tmp = objectos.copy()
    for obj in objectos:
        if obj[2] <= capacidade:
            tmp.remove(obj)
            r = max(r, obj[1]+ladraoRec(capacidade-obj[2], tmp))
    return r