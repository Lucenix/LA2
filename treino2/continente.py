def bfs(grafo, pais):
    vis = {pais}
    queue = [pais]
    while queue:
        v = queue.pop(0)
        for adj in grafo[v]:
            if adj not in vis:
                queue.append(adj)
                vis.add(adj)
    return len(vis)

def maior(vizinhos):
    grafo = {}
    for vizinho in vizinhos:
        for pais in vizinho:
            if pais not in grafo:
                grafo[pais] = set(vizinho)
            else:
                grafo[pais] = grafo[pais].union(set(vizinho))
            grafo[pais].remove(pais)
    max = 0
    for pais in grafo:
        r = bfs(grafo,pais)
        if max<r:
            max = r
    return max