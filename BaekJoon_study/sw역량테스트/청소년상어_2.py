# 물고기 이동에 굉장히 많은 영감을 준 블로그
# https://developer-ellen.tistory.com/68

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



fish_move()
print(g)

def eat():
    
