#def memo 100%
def probabilidadeMemo(passos, probs, dic, pos):
    if pos not in dic:
        dic[pos] = {0:0}
    if passos in dic[pos]:
        return dic[pos][passos]
    if ((pos[0] + pos[1]) % 2) != (passos % 2):
        dic[pos][passos] = 0
        return 0
    else:
        dic[pos][passos] = probabilidadeMemo(passos-1, probs,dic, (pos[0],pos[1] + 1)) * probs['U'] + probabilidadeMemo(passos-1, probs, dic, (pos[0],pos[1] - 1)) * probs['D'] + probabilidadeMemo(passos-1, probs, dic, (pos[0] - 1,pos[1])) * probs['L'] + probabilidadeMemo(passos-1, probs, dic, (pos[0] + 1,pos[1])) * probs['R'] 
        return dic[pos][passos]

def probabilidade(passos,probs):
    if passos==0:
        return 1
    if passos%2==1:
        return 0
    dic = {(0,0):{0:1}}
    return round(probabilidadeMemo(passos, probs,dic,(0,0)), 2)

#def rec 70%
def probabilidadeRec(passos, probs, pos):
    if passos == 0:
        if pos[0] == 0 and pos[1] == 0:
            return 1
        else:
            return 0
    elif ((pos[0] + pos[1]) % 2) != (passos % 2):
        return 0
    else:
        return probabilidadeRec(passos-1, probs, (pos[0],pos[1] + 1)) * probs['U'] + probabilidadeRec(passos-1, probs, (pos[0],pos[1] - 1)) * probs['D'] + probabilidadeRec(passos-1, probs, (pos[0] - 1,pos[1])) * probs['L'] + probabilidadeRec(passos-1, probs, (pos[0] + 1,pos[1])) * probs['R'] 

def probabilidade(passos,probs):
    if passos == 0:
        return 1
    if passos%2 == 1:
        return 0
    else:
        return round(probabilidadeRec(passos-1, probs, (0,1)) * probs['U'] + probabilidadeRec(passos-1, probs, (0,-1)) * probs['D'] + probabilidadeRec(passos-1, probs, (-1,0)) * probs['L'] + probabilidadeRec(passos-1, probs, (1,0)) * probs['R'],2)