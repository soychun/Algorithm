n,m,v_1 = map(int, input().split())
g = dict()
for i in range(m):
    a,b = map(int,input().split())
    g[a] = g.get(a,[])+[b]
    g[b] = g.get(b, []) + [a]
print(g)
print('dfs')

def dfs(g,v_1):
    v=[0]*(n+1)
    s = [v_1]
    v[v_1] = 1
    print(v_1,end=' ')
    while s:
        n_c = s.pop()
        if v[n_c]==0:
            v[n_c]=1
            print(n_c,end=' ')
        for n_a in sorted(g[n_c],reverse=True):
            if v[n_a]==0:
                s.append(n_a)
dfs(g,v_1)
print()
print('bfs')

def bfs(g,v_1):
    from collections import deque
    v = [0]*(n+1)
    v[v_1]=1
    s = deque([v_1])
    print(v_1)
    while s:
        n_c = s.popleft()
        for n_a in sorted(g[n_c]):
            if v[n_a]==0:
                v[n_a]=1
                s.append(n_a)
                print(n_a)
bfs(g,v_1)
'''
5 5 3
5 4
5 2
1 2
3 4
3 1
{5: [4, 2], 4: [5, 3], 2: [5, 1], 1: [2, 3], 3: [4, 1]}
dfs
3 1 2 5 4 
bfs
3 1 4 2 5 
'''

