def hacker(log):
    dic = {}
    for num,email in log:
        if email not in dic:
            dic[email] = list(num)
        else:
            for i in range(len(num)):
                if num[i] != '*':
                    dic[email][i] = num[i]
    
    listy = ["".join(dic[x]) for x in dic]
    return sorted(zip(listy,dic), key = lambda n: (n[0].count('*'), n[1]))