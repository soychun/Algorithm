n = 3
r = 8
n_list = [i+1 for i in range(n)]
v = [0]*n
s = []
cnt = 0
print(n_list)
순열
def dfs(L):   #ch에 있다면, 돌면서 넣고 빼고
    if L == r:
        print(s)
    else:
        for i in range(n):
            if v[i]==0:
                v[i] = 1
                s.append(n_list[i])
                dfs(L+1)
                v[i] = 0
                s.pop()
dfs(0)

조합
def dfs(L,B):  # 지정해주는거부터 돌면서 넣고 빼고
    if L==r:
        print(s)
    else:
        for i in range(B,n):
            s.append(n_list[i])
            dfs(L+1,i+1)
            s.pop()
dfs(0,0)

중복 순열 순열인데 visited체크 안함
def dfs(L):
    if L == r:
        print(s)
    else:
        for i in range(n):
            s.append(n_list[i])
            dfs(L+1)
            s.pop()

dfs(0)


중복조합  : 조합에서 현재꺼도 선택 가능하게 하는 것. 조합은
def dfs(L,B):
    global cnt
    if L==r:
        cnt+=1
        print(s)
    else:
        for i in range(B,n):
            s.append(n_list[i])
            dfs(L+1,i)
            s.pop()
dfs(0,0)
print(cnt)