# DFS라는 사실을 또 잊음
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
g = []
for i in range(n):
    # print(i)
    g.append(list(map(int,input().strip())))
# print(g)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
cnt =0
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if g[x][y]==1:
        g[x][y]=0
        global cnt
        cnt +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

cnt_list  =[]



for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result+=1
            cnt_list.append(cnt)
            cnt = 0
print(result)
cnt_list.sort()
for i in range(result):
    print(cnt_list[i])


