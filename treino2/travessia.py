def dijkstra(adj,o, pai, dist):
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        moves = [(v[0]+x[0], v[1]+x[1]) for x in [(0,1),(1,0),(0,-1),(-1,0)]]
        move = filter(lambda x: x[1]>0 and x[1]< len(adj) and x[0]>=0 and x[0]< len(adj[0]) and abs(int(adj[x[1]][x[0]]) - int(adj[v[1]][v[0]]))<=2, moves)
        for d in move:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + abs(int(adj[d[1]][d[0]]) - int(adj[v[1]][v[0]])) + 1 < dist[d]:
                pai[d] = pai[v]
                dist[d] = dist[v] + abs(int(adj[d[1]][d[0]]) - int(adj[v[1]][v[0]])) + 1

def travessia(mapa):
    ny = len(mapa)
    nx = len(mapa[0])
    dist = {}
    for end in [(x, ny-1) for x in range(0,nx)]:
        dist[end] = float("inf")
    pai = {}
    for start in [(x,0) for x in range(0,nx)]:
        pai[start] = start
        dijkstra(mapa, start, pai, dist)
    r = min([(x,ny-1) for x in range(0,nx)], key = lambda n: dist[n])
    return (pai[r][0], dist[r])

#80% falta cenas aqui ns oq
def dijkstra(adj,ori, pai, dist):
    for o in ori:
        dist[o] = 0
        pai[o] = o
    orla = set(ori)
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        if v[1] == len(adj)-1:
            return v
        moves = [(v[0]+x[0], v[1]+x[1]) for x in [(0,1),(1,0),(0,-1),(-1,0)]]
        move = filter(lambda x: x[1]>=0 and x[1]< len(adj) and x[0]>=0 and x[0]< len(adj[0]) and abs(int(adj[x[1]][x[0]]) - int(adj[v[1]][v[0]]))<=2, moves)
        for d in move:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + abs(int(adj[d[1]][d[0]]) - int(adj[v[1]][v[0]])) + 1 < dist[d]:
                pai[d] = pai[v]
                dist[d] = dist[v] + abs(int(adj[d[1]][d[0]]) - int(adj[v[1]][v[0]])) + 1
            
def travessia(mapa):
    dist = {}
    pai = {}
    r = dijkstra(mapa, [(x,0) for x in range(0,len(mapa[0]))], pai, dist)
    return (pai[r][0], dist[r])