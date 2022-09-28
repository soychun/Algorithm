n,m = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[False]*(m) for _ in range(n)]

x,y,d = map(int,input().split())
g= [ ]
for _ in range(n):
    g.append(list(map(int,input().split())))
cnt = 0
visited[x][y] = True
while True:
    tmp_d = d

    for i in range(4):
        d = (d + 1) % 4  # d업데이트, 왼쪽부터 시작
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny]==False:
                visited[nx][ny] = True
                x = nx
                y = ny
                cnt+=1
                break
            else:
                flag

        else:
            break

