dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
g = []

cnt_max = 0

for i in range(4):
    tmp = list(map(int,input().split()))
    g.append([[tmp[i*2],tmp[i*2+1]-1] for i in range(4)])
print(g)

g[0][0][0] = -1 #상어가 물고기를 먹음
print(g)
def fish_move():
    for i in range(16+1):
        for x in range(4):
            for y in range(4):
                if g[x][y][0]==i:
                    print(i)
                    b = g[x][y][1]
                    for b_ in range(8):

                        nx = x + dx[b]
                        ny = y + dy[b]
                        if 0<=nx<4 and 0<=ny<4 and (g[nx][ny][0]!=-1):
                            g[x][y],g[nx][ny] = g[nx][ny],g[x][y]
                        else:
                            b+=1


fish_move()