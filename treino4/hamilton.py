
# testa se o candidato c está completo
def complete(p,c):
    return len(p) == 0
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c,g):
    if len(c) == 0:
        return p
    else:
        l = list()
        for x in p:
            if x in g[c[-1]]:
                if len(p) == 1:
                    if c[0] in g[x]:
                        return [x]
                else:
                    l.append(x)
        return l
# testa se um candidato c é uma solução válida para p
def valid(p,c,g):
    return True
# procurar solução para p com pesquisa exaustiva

def aux(p,c,g):
    if complete(p,c):
        return valid(p,c,g)
    for x in extensions(p,c,g):
        c.append(x)
        p.remove(x)
        if aux(p,c,g):
            return True
        c.pop()
        p.append(x)
    return False

def hamilton(arestas):
    grafo = dict()
    for a,b in arestas:
        if a not in grafo:
            grafo[a] = set()
        if b not in grafo:
            grafo[b] = set()
        grafo[b].add(a)
        grafo[a].add(b)
    c = []
    if aux(list(grafo.keys()), c, grafo):
        return c
    return None