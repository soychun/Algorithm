# 첫번째, 내가 기출중에 처음으로 성공한 문제. 하지만 솔루션 필요해 보임
# 백준상으로는 pypy로 해야만 시간 초과가 안되는 이슈가 있었음

import math
import sys
input = sys.stdin.readline
R,C,T = map(int,input().split())
g = []
for _ in range(R):
    g.append(list(map(int, input().strip().split())))

# print(R,C,T)
# print(g)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dust(g):
    cc = []
    tmp = [[0 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j]>0:
                s_amount = math.floor(g[i][j]/5)
                cnt = 0

                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]

                    if 0<=ni<R and 0<=nj<C and (g[ni][nj]!=-1) :
                        # print('index: ', ni, nj)
                        cnt+=1
                        tmp[ni][nj]+=s_amount

                tmp[i][j] += g[i][j]-s_amount*cnt
            elif g[i][j] ==-1:
                cc.append(i)
                tmp[i][j] =-1

    return tmp, sorted(cc)
def wind(cc,g):
    tmp = [[0 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        for j in range(C):
            tmp[i][j] = g[i][j]
    for i in range(1,C-1+1):
        tmp[0][i-1] = g[0][i]
        tmp[R-1][i-1] = g[R-1][i]
    for i in range(1,C-2+1):
        # print(i)
        tmp[cc[0]][i+1] = g[cc[0]][i]
        tmp[cc[1]][i + 1] = g[cc[1]][i]
    for i in range(1,cc[0]+1):
        tmp[i-1][C-1] = g[i][C-1]
    for i in range(cc[1],R-2+1):
        tmp[i+1][C-1] = g[i][C-1]
    for i in range(0,cc[0]-2+1):
        tmp[i+1][0] = g[i][0]
    for i in range(cc[1]+2,R-1+1):
        tmp[i-1][0] = g[i][0]
    tmp[cc[0]][1] = 0
    tmp[cc[1]][1] = 0
    return tmp
for t in range(T):
    g,cc = dust(g)
    # print(g)
    # print(cc)
    g = wind(cc,g)
# print(g)
cnt = 0
for i in range(R):
    for j in range(C):
        cnt += g[i][j]
print(cnt+2)