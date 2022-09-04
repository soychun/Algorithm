import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
queue = deque()

n,m,s = map(int,input().split())
g = [[] for _ in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
cnt_dfs = 1
cnt_bfs = 1
for _ in range(m):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(visited_dfs,g,s):
    global cnt_dfs
    visited_dfs[s] = cnt_dfs
    cnt_dfs+=1
    print(s,end=' ')
    for s_ in sorted(g[s]):
        if visited_dfs[s_] == 0:
            dfs(visited_dfs,g,s_)

def bfs(visited_bfs,g,s):
    global cnt_bfs
    visited_bfs[s] = cnt_bfs
    cnt_bfs+=1
    print(s, end=' ')
    queue = deque()
    queue.append(s)
    while queue:
        s_ = queue.popleft()
        for i in sorted(g[s_]):
            if visited_bfs[i] == 0:
                visited_bfs[i] = cnt_bfs
                cnt_bfs+=1
                print(i, end=' ')
                queue.append(i)
dfs(visited_dfs,g,s)
print()
bfs(visited_bfs,g,s)
# print(visited_dfs)
# print(visited_bfs)
