def distancia(mapa,o,d):
    if mapa[o[1]][o[0]] != 'X':
        return None
    dist = {}
    dist[o] = 0
    if mapa[d[1]][d[0]] == 'X':
        dist[d] = float("inf")
    else:
        return None
    orla = [o]
    
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        if v == d:
            return dist[d]
        moves = [(v[0]+x[0], v[1]+x[1]) for x in [(0,1),(1,0),(0,-1),(-1,0)]]
        fmove = filter(lambda x: x[1]>=0 and x[1]< len(mapa) and x[0]>=0 and x[0]< len(mapa[0]) and (mapa[x[1]][x[0]] == 'X' or mapa[x[1]][x[0]] == '#'), moves)
        for move in fmove:
            if move not in dist:
                orla.append(move)
                dist[move] = float("inf")
            if dist[v] + 1 < dist[move]:
                dist[move] = dist[v] + 1
    return dist[d]