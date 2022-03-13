#versão com lista que se vai enchendo
def formula1(log):
    ha = {}
    sets = set()
    mintemp = -1
    for entry in sorted(log):
        if mintemp == -1:
            mintemp = entry[0]
            
        if (entry[0] - ha.get(entry[1], 0))<=mintemp:
            if (entry[0] - ha.get(entry[1], 0))<mintemp:
                sets.clear()
                mintemp = entry[0] - ha[entry[1]]
            sets.add(entry[1])
            
        ha[entry[1]] = entry[0]
    return sorted(sets)


#versão OG
def formula1(log):
    ha = {}
    flag = 1
    for entry in sorted(log):
        if entry[1] not in ha:
            ha[entry[1]] = [entry[0], entry[0]]
            if flag == 1:
                mintemp = entry[0]
                flag = 0
            elif mintemp > entry[0]:
                mintemp = entry[0]
                
        elif((entry[0] - ha[entry[1]][1])<ha[entry[1]][0]):
            ha[entry[1]][0] = entry[0] - ha[entry[1]][1]
            if mintemp > entry[0] - ha[entry[1]][1]:
                mintemp = entry[0] - ha[entry[1]][1]
        
        ha[entry[1]][1] = entry[0]
        
    return list(filter(lambda n: ha[n][0]==mintemp,sorted(ha)))