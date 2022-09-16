n,m = map(int,input().split())

n = [i for i in range(1,n+1)]

def dfs(L,B):
    if m==len(s):
        print(' '.join(map(str,s)))
    else:
        for i in range(B,len(n)):
            # print(i)
            if v[i]:
                continue
            else:
                s.append(n[i])
                dfs(L+1,i+1)
                s.pop()


s = []
v = [False]*len(n)
dfs(0,0)