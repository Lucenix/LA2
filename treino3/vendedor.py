#def dynamic 100%
def vendedor(capacidade,produtos):
    ht = {0:[]}
    mx = {0:0}
    for c in range(1, capacidade+1):
        ht[c] = []
        mx[c] = 0
        for n,v,p in produtos:
            if c-p in ht:
                if v+mx[c-p] > mx[c]:
                    mx[c] = v+mx[c-p]
                    ht[c] = ht[c-p].copy()
                    ht[c].append(n)
    return (mx[capacidade],sorted(ht[capacidade]))