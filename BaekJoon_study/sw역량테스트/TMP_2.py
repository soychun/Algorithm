import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,cm,tmp_g,rainbow_list):
    global cnt_g
    visited[x][y] = cnt_g
    tmp_g.append([x,y])
    for i in range(4):

        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny]==cm and visited[nx][ny]==0:
                dfs(nx,ny,cm,tmp_g,rainbow_list)
            elif g[nx][ny]==0 and visited[nx][ny]==0:
                rainbow_list.append([nx,ny])
                dfs(nx, ny, cm, tmp_g,rainbow_list)

            else:
                continue
        else:
            continue

def gravity(g):

    for i in range(n-2,-1,-1):
        for j in range(n):
            if g[i][j]>-1:
                r = i
                while True:
                    if 0<=r+1<n and g[r+1][j]==-2:
                        # g[r+1][j],g[r][j] = g[r][j],g[r+1][j]
                        g[r + 1][j] = g[r][j]
                        g[r][j] = -2
                        r+=1
                    else:
                        break



result = 0

while True:
    if n>30 or n<1 or m<1 or m>5:
        break
    visited = [[0] * n for _ in range(n)]
    cnt_g = 0
    g_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j]>0 or g[i][j]<=0:
                continue
            else:
                cnt_g+=1
                tmp_g = []
                rainbow_list = []
                dfs(i,j,g[i][j],tmp_g,rainbow_list)
                g_list.append([[i,j],tmp_g,len(rainbow_list)])
                for r in rainbow_list:
                    visited[r[0]][r[1]] = 0

    g_list = sorted(g_list, key=lambda x:(-len(x[1]),-x[2],-x[0][0],-x[0][1]))
    if len(g_list[0][1])==1:
        break
    result = result+ (len(g_list[0][1]))*(len(g_list[0][1]))

    for index in g_list[0][1]:
        g[index[0]][index[1]] = -2


    gravity(g)


    g = list(map(list,zip(*g)))[::-1]


    gravity(g)

print(result)