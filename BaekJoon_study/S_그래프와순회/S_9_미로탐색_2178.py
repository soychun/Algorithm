import sys
sys.setrecursionlimit(10**9)
input= sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
g =[]
for _ in range(n):
    g.append(list(map(int,input().strip())))
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 1
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if g[nx][ny] ==0:
                continue
            if g[nx][ny] ==1:
                g[nx][ny]= g[x][y]+1
                queue.append((nx,ny))
    return g[n-1][m-1]
k = bfs(0,0)
print(k)
# print(g)
