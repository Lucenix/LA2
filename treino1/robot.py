def robot(comandos):
    lista = []
    pos = [0,0]
    move = [(0,1), (-1, 0), (0,-1), (1,0)]
    maxs = [0,0,0,0]
    dir = 0
    for c in comandos:
        if c == 'A':
            pos[0] += move[dir][0]
            pos[1] += move[dir][1]
            #maxs[0] = max(maxs[0], pos[1])
            #maxs[1] = min(maxs[1], pos[0])
            #maxs[2] = min(maxs[2], pos[1])
            #maxs[3] = max(maxs[3], pos[0])
            if move[dir][(dir+1)%2]*(maxs[dir]) < move[dir][(dir+1)%2]*(pos[(dir+1)%2]):
                maxs[dir] = pos[(dir+1)%2]
        elif c == 'E':
            dir = (dir+1)%4
        elif c == 'D':
            dir = (dir-1)%4
        elif c == 'H':
            lista.append((maxs[1], maxs[2], maxs[3], maxs[0]))
            pos = [0,0]
            maxs = [0,0,0,0]
            dir = 0
    return lista