# 첫번째, 내가 기출중에 처음으로 성공한 문제. 하지만 솔루션 필요해 보임
# 백준상으로는 pypy로 해야만 시간 초과가 안되는 이슈가 있었음
# https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-17144-%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80-%EC%95%88%EB%85%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# 위에 블로그가 가장 깔끔하게 짜 두었음
# https://kyun2da.github.io/2021/04/20/brownsmog/  : 참고할 만한 블로그
# https://yuuj.tistory.com/96 : 설명 기억나지 않을 떄 참고고
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
                s_amount = math.floor(g[i][j]/5)    # 몫과 나머지로 풀이도 가능하다.
                cnt = 0

                for k in range(4):
                    ni = i+dx[k]
                    nj = j+dy[k]

                    if 0<=ni<R and 0<=nj<C and (g[ni][nj]!=-1) :
                        # print('index: ', ni, nj)
                        cnt+=1
                        tmp[ni][nj]+=s_amount

                tmp[i][j] += g[i][j]-s_amount*cnt  # g는 그대로 놔두고 남은 미세먼지만 할당, 추가로 퍼진 미세먼지만 tmp에 넣어도 됨.
            elif g[i][j] ==-1:
                cc.append(i)
                tmp[i][j] =-1

    return tmp, sorted(cc)

# 참고한 코드
def wind_top():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]   # 방향은 회오리 방향
    x,y,d = cc[0],1,0
    pre = 0             # 이를 통해서 스위칭 해줄 것이다
    while True:
        nx = x+dx[d]
        ny = y+dy[d]    # 다음거를 미리 보기
        if nx==cc[0] or ny==0:
            break       # 공기 청정기가 나오면 다음꺼 생각 안해도 됨 (이전꺼를 땅겨쓰지 않는다)
        if nx<0 or nx>=R or ny<0 or ny>=C:   # 회오리를 지정했으니, 다음꺼 (nx)가 범위를 벗어니는지만 확인해 주면 됨
            d+=1    #방향 바꾸기
            continue
        g[x][y],pre = pre,g[x][y]
        x = nx
        y = ny
def wind_bottom():



# 원래 내가 짰던, 맞았지만 복잡했던 코드
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