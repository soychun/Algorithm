n = 7
g = [[0, 1, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 1],
[0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 0, 0, 0]]

from collections import deque

v = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = []

def bfs(v,g,index):
    cnt = 1

    v[index[0]][index[1]] = 1
    q = deque()
    q.append([index[0],index[1]])

    while q:
        r,c = q.popleft()
        v[r][c] = 1
        for k in range(4):
            nx = r+dx[k]
            ny = c+dy[k]
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==1 and v[nx][ny]==0:
                q.append([nx,ny])
                v[nx][ny]=1
                cnt+=1
    count.append(cnt)


for i in range(n):
    for j in range(n):
        if g[i][j] == 1 and v[i][j] == 0:
            bfs(v,g,[i,j])
print(count)

