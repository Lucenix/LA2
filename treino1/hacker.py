def hacker(log):
    dic = {}
    for num,email in log:
        if email not in dic:
            dic[email] = list(num)
        else:
            for i in range(len(num)):
                if num[i] != '*':
                    dic[email][i] = num[i]
    
    return sorted(map(lambda n : ("".join(dic[n]), n), dic), key = lambda n: (n[0].count('*'), n[1]))