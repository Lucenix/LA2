def cruzamentos(ruas):
    dic = {}
    for rua in ruas:
        if rua[0] not in dic:
            dic[rua[0]] = 0
        dic[rua[0]] += 1
        
        if rua[0] != rua[-1]:
            if rua[-1] not in dic:
                dic[rua[-1]] = 0
            dic[rua[-1]] += 1
    return sorted(dic.items(), key = lambda n : (n[1], n[0]))