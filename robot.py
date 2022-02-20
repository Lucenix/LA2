import math

def robot(comandos):
    i = 0
    n = len(comandos)
    lista = []
    direcoes = [(0,1), (-1,0), (0,-1), (1,0)]
    while(i<n):
        pos = [0,0]
        vals = [0,0,0,0]
        dir = 0
        while(i<n and comandos[i] != 'H'):
            if(comandos[i] == 'A'):
                pos[0] += direcoes[dir][0]
                pos[1] += direcoes[dir][1]
                if vals[dir] < abs(pos[(dir+1)%2]):
                    vals[dir] = abs(pos[(dir+1)%2])
            if(comandos[i] == 'E'):
                dir = (dir + 1)%4
            if(comandos[i] == 'D'):
                dir = (dir - 1)%4
            i += 1
        lista.append((-vals[1], -vals[2], vals[3], vals[0]))
        i += 1
    return lista