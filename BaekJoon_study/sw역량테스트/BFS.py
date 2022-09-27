# https://kimjingo.tistory.com/205
BFS 는 재귀가 아니다!
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

n = 4
def out_of_range(y,x):
    return y < 0 or x < 0 or y >= n or x >= n    # 나갔니?


def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited = [[False]*n for _ in range(n)]
    visited[y][x] = True

    while q:
        s_y, s_x = q.popleft()
        for d in range(4):
            ny = s_y+dy[d]
            nx = s_x+dx[d]

            if out_of range(ny,nx) or visited[ny][nx]:
                continue  #격자에서 벗어났거나 방문한 좌표의 경우 continue
            else :
                 do_something()
                 q.append((ny,nx))
                 visited[ny][nx] = True