def horario(ucs,alunos):
    lista = []
    for aluno in sorted(alunos):
        dic = {}
        fail = 0
        total = 0
        for uc in alunos[aluno]:
            if uc in ucs and not fail:
                hora = ucs[uc][1]
                dur = ucs[uc][2]
                total += dur
                if ucs[uc][0] not in dic:
                    dic[ucs[uc][0]] = [(hora, hora + dur)]
                else:
                    for intervalo in dic[ucs[uc][0]]:
                        if hora >= intervalo[0] or hora+dur<=intervalo[1] or (hora<=intervalo[0] and hora+dur>=intervalo[1]):
                            fail = 1
                        break
                    else:
                        dic[ucs[uc][0]].append((hora,hora+dur))
            else:
                fail = 1
                break
        if not fail:
            lista.append((aluno, total))
    return sorted(lista, key = lambda n: n[1], reverse = True)