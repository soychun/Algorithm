def print_g(g):
    for i in range(len(g)):
        print(g[i])
import copy

m,S = map(int,input().split())
g = [[[] for _ in range(4)] for _ in range(4)]
print_g(g)
for i in range(m):
    r,c,d = map(int,input().split())
    g[r-1][c-1].append(d-1)
sx,sy = map(int, input().split())
sx = sx-1
sy = sy-1
print_g(g)
print('======')

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
        print('tmpxy : ',tmpsx,tmpsy)
        tmpsx_, tmpsy_ = tmpsx,tmpsy
        cnt = 0
        tmp_bag = []
        tmp_bag.append([tmpsx_, tmpsy_ ])
        if len(g_move[tmpsx][tmpsy]) > 0:
            for j in range(len(g_move[tmpsx][tmpsy])):
                cnt = cnt + g_move[tmpsx][tmpsy][j]
        for i in range(3):

            nx = tmpsx_ + dx_s[s[i] - 1]
            ny = tmpsy_ + dy_s[s[i] - 1]
            print(nx, ny, tmp_bag, '--', len(tmp_bag))
            if nx >= 4 or nx < 0 or ny >= 4 or ny < 0:

                cnt = -1
                break
            elif len(tmp_bag) > 1 and (nx == tmp_bag[-2][0] and ny == tmp_bag[-2][1]):
                tmp_bag.append([nx, ny])
                tmpsx_ = nx
                tmpsy_ = ny
            else:
                tmp_bag.append([nx, ny])
                tmp = g_move[nx][ny]
                if len(tmp) > 0:

                    for j in range(len(tmp)):
                        cnt = cnt + 1
                tmpsx_ = nx
                tmpsy_ = ny


        print(s,cnt)
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

    print('magic',s)
    print(sx,sy)
    g_1 = copy.deepcopy(g)
    g_move = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if len(g[x][y])>0:
                print(x,y,g[x][y])
                for i in range(len(g[x][y])):
                    print('da  : ',g[x][y][i])
                    for j in range(8,0,-1):
                        d = (g[x][y][i]+j)%8
                        print('tmp',d)
                        nx = x + dx[d]
                        ny = y + dy[d]
                        print(sx, sy, (nx == sx and ny == sy))
                        if (0<=nx<4 and 0<=ny<4) and not(nx==sx and ny==sy) and (s_smell[nx][ny]==0):
                            g_move[nx][ny].append(d)

                            print('----',nx,ny,d)

                            break
                        if j==1:
                            g_move[x][y].append(g[x][y][i])
                            print('n----',x, y, g[x][y][i])

    print_g(g_move)
    s_list = []
    tmpsx = sx
    tmpsy = sy
    print(tmpsx, tmpsy)
    dfs(0,[],max)
    print(sorted(s_list, key=lambda x: (-x[1])))
    tmp_s_d = sorted(s_list,key=lambda x:(-x[1]))[0]
    print(tmpsx,tmpsy)
    print(sx, sy)
    print('=======')

    for i in range(4):
        print(sx,sy)
        if len(g_move[sx][sy])>0:
            s_smell[sx][sy] = s_smell[sx][sy]+3
            g_move[sx][sy] = []
        if i==3:
            break
        else:
            sx = sx+dx_s[tmp_s_d[0][i]-1]
            sy = sy+dy_s[tmp_s_d[0][i]-1]
    print('=======')
    print(sx,sy)
    print_g(g_move)
    print_g(s_smell)
    print_g(g_move)
    print_g(g)
    g = array_add(g,g_move)
    print('after')

    print_g(g)
    for i in range(4):
        for j in range(4):
            if s_smell[i][j]>0:
                s_smell[i][j] = s_smell[i][j]-1
    print_g(s_smell)



cnt_result = count_fish(g)
print(cnt_result)

# cnt = 0
# for j in range(4):
#     for k in range(5):
#         print( j, k)
#         cnt+=1
#         if cnt ==6:
#             print('done')
#             break
#         if k==2:
#             print('no')
#     print('---',j)
