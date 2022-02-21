#super ingenuo, tentar fazer uma fun que dê parse melhor ao codigo aka escreva apenas o que vale a pena
def formata(codigo):
    build = ""
    space = 0
    n = len(codigo)
    i = 0
    while(i<len(codigo)-1):
        c = codigo[i]
        if c == '{' or c == ';':
            if c == '{':
                space+=2
            c +='\n'
            for j in range(0,space):
                c+=' '
            while(codigo[i+1] == ' '):
                i+=1
        elif c == '}':
            space -=2
            build = build[:-2]
            if space > 0:
                c+='\n'
        build += c
        i+=1
    if codigo[n-1] == '}':
        build = build[:-2]
    
    return build+codigo[n-1]
