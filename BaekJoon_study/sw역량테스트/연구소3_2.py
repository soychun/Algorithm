# https://mygumi.tistory.com/352
# 비활성화 바이러스가 그냥 빈칸이 아니라는 점을 놓침
n,m = map(int,input().split())


g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
# print(g)
b_loc = []
g_result = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j]==1:
            g_result[i][j] = '-'
        elif g[i][j]==2:
            b_loc.append([i,j])
# print(b_loc)
min_t = 1000000000
# print(g_result)
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# print('====================================================================')

# s = [[1, 5], [4, 3], [6, 0]]
# cnt_zero = 0
def count_zero(g_result):
    cnt = 0
    for i in g_result:
        cnt+=i.count(0)
    return cnt


def spread(s,g_result,cnt,cnt_zero,g):
    # global cnt_zero
    s_ = []
    for i in s:
        # print(i)
        for j in range(4):
            nx = i[0] +dx[j]
            ny = i[1] +dy[j]
            if 0<=nx<n and 0<=ny<n and g[nx][ny]==0 and g_result[nx][ny]==0 :
                g_result[nx][ny] = cnt
                # print(g_result)
                s_.append([nx,ny])
    if len(s_)==0:
        # print(count_zero(g_result))
        if count_zero(g_result)>len(b_loc):
            cnt_zero = 1000

            return cnt_zero
        else:
            cnt_zero = cnt-1
            return cnt_zero
        # return cnt_tmp
    cnt_zero = spread(s_,g_result,cnt+1,cnt_zero,g)
    # print('why')
    return cnt_zero

# a = spread(s,g_result,1,cnt_zero)
# print('yeah',spread(s,g_result,1,0))












# print('====================================================================')
import copy
def dfs(s,D,g_result,g):

    global min_t
    if len(s)==m:
        # print(s,'--',[x for x in b_loc if x not in s])
        g_result = copy.deepcopy(g_result)
        g = copy.deepcopy(g)
        # print('--')
        # print(g_result)
        # print(g)
        for y in [x for x in b_loc if x not in s]:
            g[y[0]][y[1]] = 0
        # print(g)
        # cnt_zero = spread(s, g_result, 1)
        # print(spread(s,g_result,1,0))
        a = spread(s, g_result, 1,0,g)
        print(a)
        min_t = min(min_t,a)
        # print(g_result)
        return
    elif D==len(b_loc):
        return
    s.append(b_loc[D])
    dfs(s,D+1,g_result,g)
    s.pop()
    dfs(s,D+1,g_result,g)
dfs([],0,g_result,g)
if min_t ==1000:
    print(-1)
else:
    print(min_t)

#
