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

#80%
def formata(codigo):
    i = 0
    n = len(codigo)
    ident = 0
    build = ""
    while(i<n-1):
        if ident and build[-1] == '\n':
            if codigo[i] == '}':
                ident -= 2
            for j in range(0,ident):
                build += ' '
            while(codigo[i] == '\t' or codigo[i] == ' ' or codigo[i] == '\n'):
                i+=1
        build += codigo[i]
        if codigo[i] == ';' or codigo[i] == '{' or codigo[i] == '}':
            build += '\n'
            if codigo[i] == '{':
                ident += 2
            
        i+=1
    return build+codigo[n-1]