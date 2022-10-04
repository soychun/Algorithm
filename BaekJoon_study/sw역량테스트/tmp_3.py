# 5,6,8번 예제 정답 안나옴

def print_g(g):
    for i in range(len(g)):
        print(g[i])
import copy

m,S = map(int,input().split())
g = [[[] for _ in range(4)] for _ in range(4)]
for i in range(m):
    r,c,d = map(int,input().split())
    g[r-1][c-1].append(d-1)
sx,sy = map(int, input().split())
sx = sx-1
sy = sy-1
def array_add(g,g1):
    k = copy.deepcopy(g)
    for i in range(4):
        for j in range(4):
            k[i][j] = g1[i][j]+g[i][j]
    return k
def count_fish(g):
    cnt = 0
    for i in range(4):
        for j in range(4):
            if len(g[i][j])>0:
                cnt+=len(g[i][j])
    return cnt
n_s = [1,2,3,4]
def dfs(L,s,max):
    global tmpsx
    global tmpsy
    if L == 3:
        tmpsx_, tmpsy_ = tmpsx,tmpsy
        cnt = 0
        tmp_bag = []
        # tmp_bag.append([tmpsx_, tmpsy_ ])
        # if len(g_move[tmpsx][tmpsy]) > 0:
        #     for j in range(len(g_move[tmpsx][tmpsy])):
        #         cnt = cnt + 1#g_move[tmpsx][tmpsy][j]
        for i in range(3):

            nx = tmpsx_ + dx_s[s[i]-1]
            ny = tmpsy_ + dy_s[s[i]-1]

            if nx>=4 or nx<0 or ny>=4 or ny<0:

                cnt = -1
                break
            elif len(tmp_bag)>1 and (nx==tmp_bag[-2][0] and ny==tmp_bag[-2][1]):
                tmp_bag.append([nx, ny])
                tmpsx_ = nx
                tmpsy_ = ny
            else:
                tmp_bag.append([nx, ny])
                tmp = g_move[nx][ny]
                if len(tmp)>0:

                    for j in range(len(tmp)):
                        cnt = cnt+1
                tmpsx_ = nx
                tmpsy_ = ny

        s_list.append([list(s),cnt])

    else:
        for i in range(4):
            s.append(n_s[i])
            dfs(L+1,s,max)
            s.pop()


dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

dx_s = [-1,0,1,0]
dy_s = [0,-1,0,1]
s_smell = [[0]*4 for _ in range(4)]
cnt_result = 0
for s in range(S):
    print(sx,sy)
    print('g')
    print_g(g)
    g_1 = copy.deepcopy(g)
    g_move = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if len(g[x][y])>0:
                for i in range(len(g[x][y])):
                    for j in range(8,0,-1):
                        d = (g[x][y][i]+j)%8
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if (0<=nx<4 and 0<=ny<4) and not(nx==sx and ny==sy) and (s_smell[nx][ny]==0):
                            g_move[nx][ny].append(d)


                            break
                        if j==1:
                            g_move[x][y].append(g[x][y][i])
    print('g_move')
    print_g(g_move)
    s_list = []
    tmpsx = sx
    tmpsy = sy
    dfs(0,[],max)
    print(sorted(s_list,key=lambda x:(-x[1])))
    tmp_s_d = sorted(s_list,key=lambda x:(-x[1]))[0]

    for i in range(4):
        if len(g_move[sx][sy])>0:
            s_smell[sx][sy] = s_smell[sx][sy]+3
            g_move[sx][sy] = []
        if i==3:
            break
        else:
            sx = sx+dx_s[tmp_s_d[0][i]-1]
            sy = sy+dy_s[tmp_s_d[0][i]-1]

    print('eat')
    print_g(g_move)

    for i in range(4):
        for j in range(4):
            if s_smell[i][j]>0:
                s_smell[i][j] = s_smell[i][j]-1
    g = array_add(g, g_move)
    print('smell')
    print_g(s_smell)
    print('g')
    print_g(g)



cnt_result = count_fish(g)
print(cnt_result)

