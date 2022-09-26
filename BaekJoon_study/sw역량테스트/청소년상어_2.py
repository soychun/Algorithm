# 물고기 이동에 굉장히 많은 영감을 준 블로그
# https://developer-ellen.tistory.com/68
그런데 또 하다말음


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
g = []

cnt_max = 0
cnt_list = []

for i in range(4):
    tmp = list(map(int,input().split()))
    g.append([[tmp[i*2],tmp[i*2+1]-1] for i in range(4)])
print(g)

g[0][0][0] = -1 #상어가 물고기를 먹음
print(g)
s_x,s_y = 0,0
def dfs(s_x,s_y):
    global cnt_max
    for i in range(1,16+1):
        f_x,f_y = -1,-1
        for x in range(4):
            for y in range(4):
                if g[x][y][0]==i:
                    f_x,f_y = x,y
                    print(x,y)
                    break         #안바꾸고 먼저 찾기
        print(i)
        b = g[f_x][f_y][1]
                    # print(i)
                    # b = g[x][y][1]
        for b_ in range(8):
            nx = f_x + dx[b]
            ny = f_y + dy[b]
            if 0<=nx<4 and 0<=ny<4 and (g[nx][ny][0]!=-1):
                print('--')
                g[f_x][f_y],g[nx][ny] = g[nx][ny],g[f_x][f_y]
                break

            else:
                b=(b+1)%8
    d = g[s_x][s_y][1]
    p_f_eat = []
    for i in range(1, 5):
        nx = s_x + dx[d] * i
        ny = s_y + dy[d] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and g[nx][ny][0] > 0:
            p_f_eat.append([nx, ny])
    if len(p_f_eat) == 0:
        print(cnt_list)
        return
    else:
        for i in range(len(p_f_eat)):
            f_x, f_y = p_f_eat[i][0], p_f_eat[i][1]
            cnt_max += g[f_x][f_y][0]
            cnt_list.append(g[f_x][f_y][0])

            g[f_x][f_y][0] = -1

            dfs(f_x,f_y)
            cnt_max -= g[f_x][f_y][0]
            cnt_list.pop()



dfs(0,0)
print(g)
print(cnt_max)







