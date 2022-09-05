import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if g[x][y] ==1:
        g[x][y]=0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

for _ in range(t):
    m,n,k = map(int,input().split())
    g = [[0 for _ in range(m)] for _ in range(n)]
    result = 0
    for i in range(k):
        x,y = map(int,input().split())
        g[y][x] = 1
    for n_ in range(n):
        for m_ in range(m):
            if dfs(n_,m_)==True:
                result+=1
    print(result)

