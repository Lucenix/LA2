def tabela(jogos):
    dic = {}
    for e1,g1,e2,g2 in jogos:
        if e1 not in dic:
            dic[e1] = [0,0]
        if e2 not in dic:
            dic[e2] = [0,0]
        x1,y1 = dic[e1]
        x2,y2 = dic[e2]
        dic[e1][1] += g1-g2
        dic[e2][1] += g2-g1
        if g1>g2:
            dic[e1][0]+=3
        elif g1<g2:
            dic[e2][0]+=3
        else:
            dic[e1][0]+=1
            dic[e2][0]+=1
    return sorted(sorted(map(lambda x : (x, dic[x][0]), dic)), key = lambda n: (n[1], dic[n[0]]), reverse = True)