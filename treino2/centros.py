def build2(arestas):
    adj = {}
    for s in arestas:
        if s[0] not in adj:
            adj[s[0]] = {}
        if s[-1] not in adj:
            adj[s[-1]] = {}
        adj[s[0]][s[-1]] = int(s[1:-1])
        adj[s[-1]][s[0]] = int(s[1:-1])
    return adj

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

def centros(arestas):
    adj = build2(arestas)
    dist = fw(adj)
    print(dist)
    c = []
    for v in dist:
        max = -1
        for a in dist[v]:
            if a != v:
                if dist[v][a] == float("inf"):
                    return None
                if max < dist[v][a]:
                    max = dist[v][a]
        c.append((v, max))
    return list(map(lambda z: z[0], sorted(filter(lambda x: x[1] == min(c, key = lambda y: y[1])[1], c))))