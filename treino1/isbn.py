def fun(isbn):
    total = 0
    flag = False
    for c in isbn:
        total += int(c)%10 + flag*2*(int(c)%10)
        flag = not flag
    return total

def isbn1(livros):
    return list(filter(lambda n: (fun(livros[n])%10 != 0),sorted(livros)))

def isbn2(livros):
    return list(filter(lambda n: sum(map(lambda x,y: x*y, [1,3]*7, [int(x) for x in livros[n]]))%10 != 0, sorted(livros)))