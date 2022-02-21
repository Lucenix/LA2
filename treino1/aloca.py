def aloca(prefs):
    dic = {}
    lista = []
    for aluno in sorted(prefs):
        for projeto in prefs[aluno]:
            if projeto not in dic:
                dic[projeto] = aluno
                break
        else:
            lista.append(aluno)
    return lista

def aloca(prefs):
    return ([t[1] for t in sorted(prefs.items())])