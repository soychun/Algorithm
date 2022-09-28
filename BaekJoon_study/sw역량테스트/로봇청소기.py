from collections import deque
n,m = map(int,input().split())


dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[False]*(m) for _ in range(n)]

r,c,d = map(int,input().split())
g= [ ]
for _ in range(n):
    g.append(list(map(int,input().split())))
cnt = 0
def clean(x,y,d):
    global cnt
    # q = deque()
    visited[x][y] = True
    cnt+=1
    # q.append((x,y))

    clean_search(x,y,d)

def out_of(nx,ny):
    global n,m
    if nx<0 or ny<0 or ny>=m or nx>=n:
        return True
    else:
        return False

def clean_search(x,y,d):
    nx = x + dx[(d+1)%4]  # 왼쪽
    ny = y + dy[(d+1)%4]
    # for i in range(4):
    #     sx = x + dx[(d+i)%4]
    #     sy = y + dy[(d+i)%4]
    pos = 0
    if visited[nx][ny] == False:
        # d = (d+1)%4
        clean(nx, ny,(d+1)%4)
    elif g[nx][ny] == 1 or (nx<0 or ny<0 or ny>=m or nx>=n):
        # d = (d + 1) % 4
        clean_search(x,y,(d + 1) % 4)

    for i in range(4):
        nx = x + dx[(d+i)%4]
        ny = y + dy[(d+i)%4]
        if out_of(nx,ny)==True:
            pos = 1
        else:
            if visited[nx][ny] == True or g[nx][ny]==1:
                pos = 1
            else:
                pos = 0
                break




    if pos==1:
        nx = x + dx[(d+2)%4]
        ny = y + dy[(d + 2) % 4]

        if g[nx][ny]==1:
            return
        else:
            clean_search(nx, ny, (d + 1) % 4)


clean(r,c,d)
print(cnt)

g = [[0]*4 for i in range(4)]
if g[4][4]==1:
    print('wow')
else:
    print('no')