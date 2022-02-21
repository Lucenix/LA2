def fun(isbn):
    total = 0
    flag = False
    for c in isbn:
        total += int(c)%10 + 2*flag*(int(c)%10)
        flag = not flag
    return total

def isbn(livros):
    return list(filter(lambda n: (fun(livros[n])%10 != 0),sorted(livros)))