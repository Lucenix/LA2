def dijkstra(adj,o):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = [o]
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.append(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return pai

def prim(adjsorted):
    pai = {}
    cost = {}
    o = sorted(adj)[0]
    cost[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:cost[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in cost:
                orla.add(d)
                cost[d] = float("inf")
            if adj[v][d] < cost[d]:
                pai[d] = v
                cost[d] = adj[v][d]
    return pai

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist