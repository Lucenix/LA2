# testa se o candidato c está completo
def complete(p,c,i):
    return len(c) == i
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,g):
    if len(c) == 0:
        return p
    else:
        return filter(lambda x: x>=c[-1], p)
    
# testa se um candidato c é uma solução válida para p
def valid(p,c,g):
    for a,b in g:
        if a not in c and b not in c:
            return False
    return True

def aux(p,c,i,g):
    if complete(p,c,i):
        return valid(p,c,g)
    for x in extensions(p,c,g):
        c.append(x)
        if aux(p,c,i,g):
            return True
        c.pop()
    return False

def cobertura(arestas):
    grafo = {}
    for a,b in arestas:
        if a not in grafo:
            grafo[a] = set()
        if b not in grafo:
            grafo[b] = set()
        grafo[a].add(b)
    for i in range(0, len(grafo.keys())+1):
        if aux(sorted(list(grafo.keys())),[],i,arestas):
            return i