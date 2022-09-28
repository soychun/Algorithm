n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))


def print_g(g):
    for i in range(len(g)):
        print(g[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, cm, tmp_g):
    global cnt_g
    visited[x][y] = cnt_g
    tmp_g.append([x, y])
    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if (g[nx][ny] == cm or g[nx][ny] == 0) and visited[nx][ny] == 0:
                dfs(nx, ny, cm, tmp_g)
            else:
                continue
        else:
            continue


def gravity(g):
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if g[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and g[r + 1][j] == -2:
                        g[r + 1][j], g[r][j] = g[r][j], g[r + 1][j]
                        r += 1
                    else:
                        break
result = 0

while True:
    visited = [[0] * n for _ in range(n)]
    cnt_g = 0
    g_list = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0 or g[i][j] <= 0:
                continue
            else:

                cnt_g += 1
                tmp_g = []
                dfs(i, j, g[i][j], tmp_g)
                g_list.append([[i, j], tmp_g])

    g_list = sorted(g_list, key=lambda x: (-len(x[1]), -x[0][0], -x[0][1]))
    if len(g_list[0][1]) == 1:
        break

    result = result + (len(g_list[0][1])) * (len(g_list[0][1]))

    for index in g_list[0][1]:

        g[index[0]][index[1]] = -2

    gravity(g)
    g = list(map(list, zip(*g)))[::-1]


    gravity(g)

print(result)