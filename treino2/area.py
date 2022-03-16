def area(p,mapa):
    vis = set()
    count = 0
    queue = []
    
    if mapa[p[1]][p[0]] == '.':
        queue = [p]
        count+=1
        vis.add(p)
        
    while queue:
        v = queue.pop(0)
        if v[1] >= 1:
            if mapa[v[1]-1][v[0]] == '.' and (v[0], v[1]-1) not in vis:
                queue.append((v[0], v[1]-1))
                vis.add((v[0], v[1]-1))
                count += 1
        if v[1] < len(mapa)-1:
            if mapa[v[1]+1][v[0]] == '.' and (v[0], v[1]+1) not in vis:
                queue.append((v[0], v[1]+1))
                vis.add((v[0], v[1]+1))
                count += 1
        if v[0] >= 1:
            if mapa[v[1]][v[0]-1] == '.' and (v[0]-1, v[1]) not in vis:
                queue.append((v[0]-1, v[1]))
                vis.add((v[0]-1, v[1]))
                count += 1
        if v[0] < len(mapa[0])-1:
            if mapa[v[1]][v[0]+1] == '.' and (v[0]+1, v[1]) not in vis:
                queue.append((v[0]+1, v[1]))
                vis.add((v[0]+1, v[1]))
                count += 1
        
    return count