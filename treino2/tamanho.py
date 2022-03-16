def tamanho(ruas):
    dist = dict()
    for rua in ruas:
        o = rua[0]
        d = rua[-1]
        if o not in dist:
            dist[o] = {}
        if d not in dist:
            dist[d] = {}
        if o not in dist[d] or dist[o][d] > len(rua):
            dist[d][o] = len(rua)
            dist[o][d] = len(rua)
            
    for cruz1 in dist:
        dist[cruz1][cruz1] = 0
        for cruz2 in dist:
            if cruz2 not in dist[cruz1]:
                dist[cruz1][cruz2] = float("inf")
            if cruz1 not in dist[cruz2]:
                dist[cruz2][cruz1] = float("inf")
        
    for cruz2 in dist:
        for cruz1 in dist:
            for cruz3 in dist:
                if cruz1 != cruz3 and dist[cruz1][cruz2]+dist[cruz2][cruz3] < dist[cruz1][cruz3]:
                    dist[cruz1][cruz3] = dist[cruz1][cruz2]+dist[cruz2][cruz3]
    return max([dist[a][b] for a in dist for b in dist if dist[a][b] != float("inf")])