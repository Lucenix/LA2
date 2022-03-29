#chega isto, usa o indirect mas verifica para cada vértice
def erdos(artigos,n):
    dist = {"Paul Erdos":0}
    queue = ["Paul Erdos"]
    vis = {"Paul Erdos"}
    while queue:
        v = queue.pop(0)
        for artigo in artigos:
            if v in artigos[artigo]:
                for adj in artigos[artigo]:
                    if adj not in vis:
                        queue.append(adj)
                        vis.add(adj)
                        dist[adj] = dist[v] + 1
    #se pedir n para todos
    #for left in grafo:
    #    if left not in dist:
    #        dist[left] = float("inf")
    return sorted(list(filter(lambda i: dist[i]<=n, dist)), key = lambda i: (dist[i], i))


def erdosIndirect(artigos,n):
    grafo = {"Paul Erdos": []}
    for artigo in artigos:
        for pessoa in artigos[artigo]:
            if pessoa not in grafo:
                grafo[pessoa] = list()
            grafo[pessoa].append(artigo)
    dist = {}                    
    
    queue = ["Paul Erdos"]
    vis = {"Paul Erdos"}
    dist["Paul Erdos"] = 0
    last = 0
    while queue and last<=n:
        v = queue.pop(0)
        for artigo in grafo[v]:
            for adj in artigos[artigo]:
                if adj not in vis:
                    queue.append(adj)
                    vis.add(adj)
                    dist[adj] = dist[v] + 1
                    last = dist[adj]
    #se pedir n para todos
    #for left in grafo:
    #    if left not in dist:
    #        dist[left] = float("inf")
    return sorted(list(filter(lambda i: dist[i]<=n, dist)), key = lambda i: (dist[i], i))

def erdos(artigos,n):
    grafo = dict()
    for artigo in artigos:
        conj = artigos[artigo]
        for pessoa in conj:
            if pessoa not in grafo:
                grafo[pessoa] = set(conj)
            else:
                grafo[pessoa] = grafo[pessoa].union(conj)
            grafo[pessoa].remove(pessoa)
    dist = {}                    
    if "Paul Erdos" in grafo:
        queue = ["Paul Erdos"]
        vis = {"Paul Erdos"}
        dist["Paul Erdos"] = 0
        while queue:
            v = queue.pop(0)
            for adj in grafo[v]:
                if adj not in vis:
                    queue.append(adj)
                    vis.add(adj)
                    dist[adj] = dist[v] + 1
    #se pedir n para todos
    #for left in grafo:
    #    if left not in dist:
    #        dist[left] = float("inf")
    return sorted(list(filter(lambda i: dist[i]<=n, dist)), key = lambda i: (dist[i], i))