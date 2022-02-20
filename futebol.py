def tabela(jogos):
    dic = {}
    for e1,g1,e2,g2 in jogos:
        if e1 not in dic:
            dic[e1] = (0,0)
        if e2 not in dic:
            dic[e2] = (0,0)
        x1,y1 = dic[e1]
        x2,y2 = dic[e2]
        y1+=g1-g2
        y2+=g2-g1
        if g1>g2:
            x1+=3
        elif g1<g2:
            x2+=3
        else:
            x1+=1
            x2+=1
        dic[e1] = x1,y1
        dic[e2] = x2,y2
    r = sorted(zip(dic, [x[1][0] for x in dic.items()])) //ordenar pela ordem certa os nomes
    return sorted(r, key = lambda n: (n[1], dic[n[0]]), reverse = True) //ordenar pela ordem contraria pelos pontos e depois pelos golos