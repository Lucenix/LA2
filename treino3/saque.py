#def dynamic 100%
def saque(mapa):
    if len(mapa) == 0 or len(mapa[0]) == 0 or mapa[0][0] == '#':
        return 0
    c = 0
    if mapa[0][0] != '.':
        c = int(mapa[0][0])
    dic = {(0,0):c}
    for i in range(1, len(mapa[0])):
        if mapa[0][i] == '#':
            dic[(i,0)] = float('-inf')
        else:
            c = 0
            if mapa[0][i] != '.':
                c = int(mapa[0][i])
            dic[(i,0)] = c+dic[(i-1,0)]
    for j in range(1, len(mapa)):
        if mapa[j][0] == '#':
            dic[(0,j)] = float('-inf')
        else:
            c = 0
            if mapa[j][0] != '.':
                c = int(mapa[j][0])
            dic[(0,j)] = c+dic[(0,j-1)]
    
    for i in range(1, len(mapa[0])):
        for j in range(1, len(mapa)): 
            if mapa[j][i] == '#':
                dic[(i,j)] = float('-inf')
            else:
                c = 0
                if mapa[j][i] != '.':
                    c = int(mapa[j][i])
                dic[(i,j)] = c+ max(dic[(i-1,j)], dic[(i,j-1)])
        for j in range(1, len(mapa)):
            del dic[(i-1,j)]
    return dic[(len(mapa[0])-1, len(mapa)-1)]   

#def rec 50%
def saqueRec(mapa, pos):
    if (pos[0] < len(mapa[0])) and (pos[1] < len(mapa)):
        if mapa[pos[1]][pos[0]] == '#':
            return 0
        else:
            c = 0
            if mapa[pos[1]][pos[0]] != '.':
                c += int(mapa[pos[1]][pos[0]])
            return max(saqueRec(mapa, (pos[0] + 1, pos[1])), saqueRec(mapa, (pos[0], pos[1] + 1))) + c
    else:
        return 0

def saque(mapa):
    if len(mapa) == 0 or len(mapa[0]) == 0:
        return 0
    else:
        c = 0
        if mapa[0][0] != '.' and mapa[0][0] != '#':
            c += int(mapa[0][0])
        return max(saqueRec(mapa, (1,0)), saqueRec(mapa, (0,1))) + c