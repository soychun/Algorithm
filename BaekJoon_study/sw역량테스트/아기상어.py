import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0
x,y,size = 0,0,2
for i in range(n):
    for j in range(n):
        if g[i][j] ==9:
            x = i
            y = j

def biteFisht(x,y,shark_size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    temp = []
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            nx = cur_x+dx[i]
            ny = cur_y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                if graph[nx][ny] <= shark_size:
                    q.append((nx,ny))
                    visited[nx][ny] =1
                    distance[nx][ny]=distance[cur_x][cur_y]+1
                    if graph[nx][ny] < shark_size and graph
                        distance[nx][ny]

a = [(2,1,3),(1,3,3),(3,3,4),(1,1,3)]
print(sorted(a,key=lambda x: (-x[2],-x[0],-x[1])))
