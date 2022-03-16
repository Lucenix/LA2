def caminho(mapa):
    lista = []
    if mapa[0][0] != ' ':
        return lista
    vis = {(0,0)}
    pais = {}
    queue = [(0,0)]
    move = {'N':(0,-1),'E':(1,0),'S':(0,1),'O':(-1,0)}
    found = False
    while queue and not found:
        v = queue.pop(0)
        for dir in move:
            if not found and v[1]+move[dir][1] >= 0 and v[1]+move[dir][1] < len(mapa) and v[0]+move[dir][0] >= 0 and v[0]+move[dir][0] < len(mapa):
                adj = (v[0]+move[dir][0],v[1]+move[dir][1])
                if adj not in vis and mapa[adj[1]][adj[0]] == ' ':
                    queue.append(adj)
                    vis.add(adj)
                    pais[adj] = dir
                    if adj == (len(mapa)-1, len(mapa)-1):
                        found = True
    if found:
        pai = (len(mapa)-1,len(mapa)-1)
        while pai != (0,0):
            lista.append(pais[pai])
            pai = (pai[0] - move[pais[pai]][0], pai[1] - move[pais[pai]][1])
    lista.reverse()
    return "".join(lista)