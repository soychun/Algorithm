import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import deque
import copy

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().strip().split())))
print(g)

bs = 2
cnt = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y,g,x_,y_):
    h = [[0 for _ in range(len(g))] for _ in range(len(g))]
    queue = deque()
    queue.append((x,y))
    h[x][y] = 1
    global bs
    while queue:
        x,y = queue.popleft()
        print(x,y)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if g[nx][ny] > bs:
                continue
            if g[nx][ny] <= bs:
                h[nx][ny]=h[x][y]+1
                queue.append((nx,ny))
    return h

bs = 2
index_list = []
s_list = []
sorted_index_list = []
for i in range(len(g)):
    for j in range(len(g)):
        if g[i][j]<bs and g[i][j]>=1:
            index_list.append((i,j))
print(index_list)
while index_list:
    x,y = index_list.pop()
    print(x,y)
    s_list.append(bfs(2,1,g,x,y))
print(s_list)