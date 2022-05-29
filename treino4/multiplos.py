# testa se o candidato c está completo
def complete(p,c):
    return len(c) == p
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c):
    return [x for x in range(1, p+1) if x not in c]
# testa se um candidato c é uma solução válida para p
def valid(p,c,d):
    return int("".join(map(lambda i : str(i), c)))%d==0

def aux(p,c,d):
    if complete(p,c) and valid(p,c,d):
        return 1
    r = 0
    for x in extensions(p,c):
        c.append(x)
        r += aux(p,c,d)
        c.pop()
    return r
    
def multiplos(n,d):
    return aux(n,[],d)