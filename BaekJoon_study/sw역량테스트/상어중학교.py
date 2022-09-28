import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

def print_g(g):
    for i in range(len(g)):
        print(g[i])
# n = 5
# m = 3
# g = [[2, 2, -1, 3, 1],
# [3, 3, 2, 0, -1],
# [0, 0, 0, 1, 2],
# [-1, 3, 1, 3, 2],
# [0, 3, 2, 2, 1]]
# print_g(g)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,cm,tmp_g,rainbow_list):
    # print(x,y)
    global cnt_g
    # if g[x][y]>0:
    visited[x][y] = cnt_g
    tmp_g.append([x,y])
    # print('tmp_g',tmp_g)
    for i in range(4):

        nx = x+dx[i]
        ny = y+dy[i]
        # print('x,y',i,nx,ny)
        if 0<=nx<n and 0<=ny<n:
            if g[nx][ny]==cm and visited[nx][ny]==0:
                # tmp_g.append([nx,ny])
                dfs(nx,ny,cm,tmp_g,rainbow_list)
            elif g[nx][ny]==0 and visited[nx][ny]==0:
                rainbow_list.append([nx,ny])
                dfs(nx, ny, cm, tmp_g,rainbow_list)

            else:
                # print('con')
                continue
                # print('no')
        else:
            # print('out')
            continue

def gravity(g):

    for i in range(n-2,-1,-1):
        for j in range(n):
            # print(i,j)
            if g[i][j]>-1: # 아래줄부터 쭉 보다가 보다가 블럭이면
                r = i
                while True:
                    if 0<=r+1<n and g[r+1][j]==-2: #다음줄이 존재하고 빈공간이면 아래로 내려
                        #블럭이 있으면 봤기 때문에 아래가 비어도 모른다
                        # g[r+1][j],g[r][j] = g[r][j],g[r+1][j]
                        g[r + 1][j] = g[r][j]
                        g[r][j] = -2
                        r+=1
                    else:   #다음줄이 존재안하거나 블럭이거나 벽이거나
                        break
            #빈공간이면? 처리해줄 것 없음. 벽이면? 처리해줄 것 없음



result = 0

while True:
    visited = [[0] * n for _ in range(n)]
    cnt_g = 0
    g_list = []
    print_g(g)
    for i in range(n):
        for j in range(n):
            if visited[i][j]>0 or g[i][j]<=0:
                continue
            else:

                # print([i,j])
                cnt_g+=1
                tmp_g = []
                rainbow_list = []
                dfs(i,j,g[i][j],tmp_g,rainbow_list)
                # g_list.append([[i, j], list(map(list, set(map(tuple, tmp_g))))])
                g_list.append([[i,j],tmp_g,len(rainbow_list)])
                # list(map(list, set(map(tuple, a))))
                for r in rainbow_list:
                    visited[r[0]][r[1]] = 0

    g_list = sorted(g_list, key=lambda x:(-len(x[1]),-x[2],-x[0][0],-x[0][1]))     # 가장 큰 블록 찾기
    if len(g_list[0][1])==1:
        break
    print(g_list)
    result = result+ (len(g_list[0][1]))*(len(g_list[0][1]))      #점수 합산
    print(result)
    for index in g_list[0][1]:      # 블록 비우기
        # print(index)
        g[index[0]][index[1]] = -2
    print_g(g)
    print('중력')

    gravity(g)
    print_g(g)

    print('회전')

    g = list(map(list,zip(*g)))[::-1]
    print_g(g)

    print('중력')

    gravity(g)
    print_g(g)
    print('=================================')


print(result)