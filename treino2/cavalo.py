#isto não tenta caminho nenhum primeiro
def saltos(o,d):
    dist = {o:0}
    moves = [(1,2),(2,1),(1,-2),(-2,1),(-1,-2),(-2,-1),(-1,2),(2,-1)]
    queue = [o]
    vis = {o}
    while queue:
        v = queue.pop(0)
        if v == d:
            return dist[v]
        for move in moves:
            pos = (v[0] + move[0], v[1] + move[1])
            if pos not in vis:
                vis.add(pos)
                queue.append(pos)
                dist[pos] = dist[v] + 1
        
    return dist[d]



def saltosIng(o,d):
    dist = {o:0}
    #pesos = {o:d[1]+d[0]-o[1]-o[0]}
    queue = [o]
    vis = {o}
    while queue:
        v = queue.pop(0)
        #v = min(queue, key=lambda x: pesos[x])
        #queue.remove(v)
        if v == d:
            return dist[v]
            
        if d[0] <= v[0]:
            i = -2
        else:
            i = 2
            
        if (v[0]+i, v[1]+i/2) not in vis:
            queue.append((v[0]+i, v[1]+i/2))
            dist[(v[0]+i, v[1]+i/2)] = dist[v] + 1
            vis = (v[0]+i, v[1]+i/2)
            #pesos[(v[0]+i, v[1]+i/2)] = d[1] - (v[1]+i/2) + pesos[v] + d[0] - (v[0]+i)
        if (v[0]+i, v[1]-i/2) not in vis:
            queue.append((v[0]+i, v[1]-i/2))
            dist[(v[0]+i, v[1]-i/2)] = dist[v] + 1
            vis = (v[0]+i, v[1]-i/2)
            #pesos[(v[0]+i, v[1]-i/2)] = d[1] - (v[1]-i/2) + pesos[v] + d[0] - (v[0]+i)
        if (v[0]+i/2, v[1]+i) not in vis:
            queue.append((v[0]+i/2, v[1]+i))
            dist[(v[0]+i/2, v[1]+i)] = dist[v] + 1
            vis = (v[0]+i/2, v[1]+i)
            #pesos[(v[0]+i/2, v[1]+i)] = d[1] - (v[1]+i) + pesos[v] + d[0] - (v[0]+i/2)
        if (v[0]+i/2, v[1]-i) not in vis:
            queue.append((v[0]+i/2, v[1]-i))
            dist[(v[0]+i/2, v[1]-i)] = dist[v] + 1
            vis = (v[0]+i/2, v[1]-i)
            #pesos[(v[0]-i/2, v[1]+i)] = d[1] - (v[1]+i) + pesos[v] + d[0] - (v[0]-i/2)
            
        
    return dist[d]