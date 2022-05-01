#def dynamic 100%
def vendedor(capacidade,produtos):
    ht = {0:[]}
    mxs = {0:0}
    for c in range(1, capacidade+1):
        ht[c] = []
        mxs[c] = 0
        for n,v,p in produtos:
            if c-p>=0 and v+mxs[c-p] > mxs[c]:
                mxs[c] = v+mxs[c-p]
                ht[c] = ht[c-p].copy()
                ht[c].append(n)
    return (mxs[capacidade],sorted(ht[capacidade]))