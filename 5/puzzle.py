# testa se o candidato c está completo
def complete(p,c,ind,puz):
    print(ind)
    return ind == len(p)
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,ind,puz):
    r = []
    ex = p[ind]
    print(ex)
    if c[ex] == -2:
        r = [x for x in range(1,10) if x not in c.values()]
    elif c[ex] == -1:
        r = [x for x in range(0,10) if x not in c.values()]
    print(r)
    return r
# testa se um candidato c é uma solução válida para p
def valid(p,c,puz):
    string = ""
    for letra in puz:
        if letra in c:
            string+=str(c[letra])
        elif letra == '=':
            string+=letra
            string+=letra
        else:
            string+=letra
    return eval(string)
            
def aux(p,c,puz,ind):
    if complete(p,c,ind,puz):
        return valid(p,c,puz)
    for x in extensions(p,c,ind,puz):
        tmp = c[p[ind]]
        c[p[ind]] = x
        if aux(p,c,puz,ind+1):
            return True
        c[p[ind]] = tmp
    return False

def puzzle(p):
    d = dict()
    for i in range(0,len(p)):
        if (p[i] >= 'A' and p[i] <= 'Z') and p[i] not in d:
            d[p[i]] = -1
        if p[i] in d and (i == 0 or p[i-1] not in d):
            d[p[i]] = -2
    s = ""
    print(d)
    if aux(sorted(d.keys()),d,p,0):
        for x in (sorted(d.keys())):
            s += str(d[x])
    return s