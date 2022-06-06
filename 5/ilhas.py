def bfs(c,adj, o, tamanhoX, tamanhoY):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        anda = map(lambda x,y: (x[0]+y[0], x[1]+y[1]), [v]*4, [(0,1),(0,-1),(1,0),(-1,0)])
        for d in filter(lambda z: 0<=z[0]<tamanhoX and 0<=z[1]<tamanhoY,anda):
            if d not in vis:
                if adj[d[1]][d[0]] == '#':
                    vis.add(d)
                    queue.append(d)
    return vis

def ilhas(mapa):
    if not mapa:
        return 0
    tamanhoX = len(mapa[0])
    tamanhoY = len(mapa)
    cor = set()
    cori = 0
    for i,j in [(x,y) for x in range(tamanhoX) for y in range(tamanhoY)]:
        if mapa[j][i] == "#" and (i,j) not in cor:
            cori += 1
            cor = cor.union(bfs(cori, mapa, (i,j), tamanhoX, tamanhoY))
    return cori