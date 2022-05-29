def bfs(p,queue):
    vis = set(queue)
    while queue:
        v = queue.pop(0)
        if complete(p,v) and valid(p,v):
            return v
        for x in extensions(p,v):
            if x not in vis:
                queue.append(x)
                vis.add(x)
    return None