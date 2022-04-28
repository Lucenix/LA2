#def melhor? 80%
def espaca(frase,palavras):
    dic = {}
    dic[0] = ['', 0]
    n = len(frase)
    for i in range(n-1, -1, -1):
        #dic[i] = ['', 0]
        for palavra in palavras:
            if frase[i:].startswith(palavra):
                l = len(palavra)
                if i+l == n:
                    dic[i] = [palavra, l]
                if i+l in dic:
                    dic[i] = ['', 0]
                    if l > dic[i][1]:
                        dic[i] = [palavra + ' ' + dic[i+l][0], l]
    return dic[0][0]

#def iter 80%
def espaca(frase,palavras):
    dic = {}
    dic[0] = ['', 0]
    for i in range(len(frase)-1, -1, -1):
        dic[i] = ['',0]
        for palavra in palavras:
            if palavra != '':
                if frase[i:].startswith(palavra):
                    l = len(palavra)
                    if i+l == len(frase):
                        dic[i] = [palavra, l]
                    elif i+l in dic:
                        if dic[i+l][1]+l > dic[i][1]:
                            dic[i] = [palavra + ' ' + dic[i+l][0], l + dic[i+l][1]]
                
    return max(dic.values(), key=lambda n: n[1])[0]


#def rec 80%
def espaca(frase,palavras):
    return espacaRec(frase,palavras)[0]

def espacaRec(frase,palavras):
    dic = dict()
    dic[frase] = ['',0]
    #fazer uma lista com frase[len(palavra):] e sacar a menor
    for palavra in palavras:
        if frase.startswith(palavra):
            if frase[len(palavra):] not in dic:
                lis = espacaRec(frase[len(palavra):], palavras)
                if lis[0] == '':
                    dic[frase[len(palavra):]] = [palavra,lis[1]+len(palavra)]
                else:
                    dic[frase[len(palavra):]] = [palavra + ' ' + lis[0],lis[1]+len(palavra)]
    return max(dic.values(), key = lambda n: n[1])

#def memo 80%
def espacaMemo(frase,palavras,dic):
    if frase == '':
        return ''
    if frase in dic:
        return dic[frase]
    for palavra in sorted(palavras, reverse = True, key = lambda n : len(n)):
        if frase.startswith(palavra):
            tmp = espacaMemo(frase[len(palavra):], palavras, dic)
            if tmp is not None:
                dic[frase] = palavra + ' ' + tmp
                return palavra + ' ' + tmp
    dic[frase] = None
    return None

def espacaM(frase,palavras):
    dic = dict()
    for palavra in palavras:
        dic[palavra] = palavra
    tmp = espacaMemo(frase,palavras,dic)
    if tmp is None:
        return ''
    else:
        return tmp

#def rec 80%
def espacaRec(frase, palavras):
    if frase == '':
        return ''
    for palavra in sorted(palavras, reverse = True, key = lambda n: len(n)):
        if palavra != '':
            if frase.startswith(palavra):
                tmp = espacaRec(frase[len(palavra):], palavras)
                if tmp is not None:
                    if tmp == '':
                        return palavra
                    else:
                        return palavra + ' ' + tmp
    return None

def espaca(frase,palavras):
    r = espacaRec(frase, palavras)
    if r is None:
        return ''
    else:
        return r