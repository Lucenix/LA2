
def isPrime(n):
    for i in range(2, int(n/2)):
        if n%i==0:
            return False
    return True

# testa se o candidato c está completo
def complete(p,c):
    return len(c) == p
# enumera as extensões válidas para o candidato parcial c
def extensions(p,c):
    l = list()
    if c == []:
        return range(1, p+1)
    for i in range(1, p+1):
        if i not in c and isPrime(i+c[-1]):
            if len(c) != p-1 or isPrime(i+c[0]):
                l.append(i)
    return l
            
# testa se um candidato c é uma solução válida para p
def valid(p,c):
    return True
# procurar solução para p com pesquisa exaustiva

def aux(p,c):
    if complete(p,c):
        return valid(p,c)
    for x in extensions(p,c):
        c.append(x)
        if aux(p,c):
            return True
        c.pop()
    return False

def anel(n):
    c = []
    if aux(n,c):
        return c