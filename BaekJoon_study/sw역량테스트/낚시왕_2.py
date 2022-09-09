# https://pacific-ocean.tistory.com/379
# 남의 풀이 복기 내가 푼 것 아님 좀 너무 비현실적인 풀이

# https://developer-ellen.tistory.com/60
# 내가 현실적으로 풀 수 있는 풀이

dx = [-1,1,0,0]
dy = [0,0,1,-1]
R,C,m = map(int,input().split())
g = [[0]*C for i in range(R)]
for i in range(m):
    r,c,s,d,z = map(int,input().split())
    g[r-1][c-1] = [s,d-1,z]
print(g)
result = 0

def shMove():
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] !=0:
                x,y,s,d,z = i,j,g[i][j][0],g[i][j][1],g[i][j][2]
                while s>0:
                    x+=dx[d]
                    y+=dy[d]
                    if 0<=x<R and 0<=y<C:
                        s-=1
                    else:
                        x-=dx[d]
                        y-=dy[d]
                        if d==0:d=1
                        .
                        .
                        .
                if tmp[x][y]==0:
                    tmp[x][y] = []
















for i in range(C):
    for j in range(R):
        if g[j][i] !=0:
            result += g[j][i][2]
            g[j][i] = 0
            break
    g = shMove()
