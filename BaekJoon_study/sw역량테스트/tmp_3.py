n_s = [1,2,3,4]
a = []
cnt = 0
v = [0,0,0,0]
def dfs(L,s):
    global cnt
    if L == 3:
        print(s)
        a.append(list(s))
        cnt+=1
    else:
        for i in range(4):
                s.append(n_s[i])
                dfs(L+1,s)
                s.pop()

dfs(0,[])

print(a)
print(cnt)