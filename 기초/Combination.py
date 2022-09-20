n,m = map(int,input().split())

n = [i for i in range(1,n+1)]

def dfs(L,B):
    if m==len(s):
        print(s)
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
print()

# 딩코딩 코드
def DFS(L,BeginWith):
    if L==r:
        print(result)
    else:
        for i in range(BeginWith,len(n)):
            result[L] = n[i]
            DFS(L+1,i+1)
n = [1,2,3,4]
r = 3
result = [0]*r
DFS(0,0)