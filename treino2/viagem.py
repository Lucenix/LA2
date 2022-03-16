def viagem(rotas,o,d):
    dist = {o:0}
    queue = [o]
    while queue:
        v = min(queue, key = lambda n : dist[n])
        queue.remove(v)
        for rota in rotas:
            for i in range(0, len(rota)):
                if rota[i] == v:
                    idx = i-2
                    if idx>=0:
                        if rota[i-2] not in dist:
                            queue.append(rota[i-2])
                            dist[rota[idx]] = dist[v]+rota[idx+1]
                        elif dist[v]+rota[idx+1]<dist[rota[idx]]:
                            dist[rota[idx]] = dist[v]+rota[idx+1]
                    idx = i+2
                    if idx<len(rota):
                        if rota[idx] not in dist:
                            queue.append(rota[idx])
                            dist[rota[idx]] = dist[v]+rota[idx-1]
                        elif dist[v]+rota[idx-1]<dist[rota[idx]]:
                            dist[rota[idx]] = dist[v]+rota[idx-1]
    return dist[d]