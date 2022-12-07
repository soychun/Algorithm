# https://dean30.tistory.com/18

n,m,v_1 = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
print(g)
print('dfs')
def dfs(g,v_1):
    s = [v_1]
    v = [0]*(n+1)
    v[v_1] = 1
    print(v_1, end=' ')
    while s:
        n_c = s.pop()
        if v[n_c]==0:
            print(n_c, end=' ')
            v[n_c] =1
        for n_a in sorted(g[n_c],reverse=True):
            if v[n_a] == 0:
                s.append(n_a)
                # print('s', s)
dfs(g,v_1)
print()


print('recursive dfs')
v = [0]*(n+1)
def dfs_re(v_1):
    v[v_1] = 1
    print(v_1,end=' ')
    for i in sorted(g[v_1]):
        if not v[i]:
            dfs_re(i)
dfs_re(v_1)
from collections import deque
print()
print('bfs')

# def bfs(g,v_1):
#     s = deque()
#     s.append(v_1)
#     v = [0]*(n+1)
#     tmp = []
#     while s:
#         n_c = s.popleft()
#         if v[n_c]==0:
#             v[n_c] = 1
#             tmp.append(n_c)
#         for n_a in sorted(g[n_c]):
#             if v[n_a] == 0:
#                 s.append(n_a)
#     return tmp
# tmp = bfs(g,v_1)

def bfs(g,v_1):
    s = deque()
    s.append(v_1)
    print(v_1,end = ' ')
    v = [0]*(n+1)
    tmp = []
    v[v_1] = 1
    while s:
        n_c = s.popleft()
        for n_a in sorted(g[n_c]):
            if v[n_a] == 0:
                s.append(n_a)
                v[n_a]=1
                print(n_a,end =' ')
    return tmp

bfs(g,v_1)