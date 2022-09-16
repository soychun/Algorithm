def dfs(L):
    if len(s)==m:
        print(' '.join(map(str,s)))

    else:
        for i in range(len(n)):
            if v[i]:
                continue
            else:
                v[i]=True
                s.append(n[i])
                dfs(L+1)
                v[i]=False
                s.pop()
n, m = map(int, input().split())
n = [i for i in range(1,1+n)]
s = []
v = [False]*len(n)
dfs(0)