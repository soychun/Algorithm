# https://jjangsungwon.tistory.com/54
# 완전 잘 짜 놓은 코드이니 다시 확인해 볼 것

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

m = []
# for _ in range(4):
#     tmp = list(map(int,input().split()))
#     m.append([[tmp[2*i],tmp[2*i+1]-1] for i in range(4)])
# print(m)
m = [[[7, 5], [2, 2], [15, 5], [9, 7]], [[3, 0], [1, 7], [14, 6], [10, 0]], [[6, 0], [13, 5], [4, 2], [11, 3]], [[16, 0], [8, 6], [5, 1], [12, 1]]]
eat = 0

print(m)

def find_fish_1(n):
    flag = False
    print(n)
    for x in range(4):
        for y in range(4):
            if m[x][y][0]==n:
                print('flag',x,y)
                flag = True
            if flag:
                break
        if flag:
            break
    print('flag',x,y,'re')
    return x,y

def find_fish(n):#https://jjangsungwon.tistory.com/54
    print(n)
    for x in range(4):
        for y in range(4):
            if m[x][y][0]==n:
                return [x,y]
    return None
print('aa')
def move_fish_1():   #처음에 짠 코드. #1 부분의 조건이 틀렸고, #2 부분에서 while을 쓸 필요가 없다...
    for n in range(1,16+1):
        x,y = find_fish(n)
        p = m[x][y][1]
        nx = x + dx[p]
        ny = y + dy[p]
        while True: #2
            if 0 <= nx < 4 and 0 <= ny < 4 and m[nx][ny][0] != -1:  #1
                m[x][y],m[nx][ny] = m[nx][ny],m[x][y]
                break
            else:
                p=(p+1)%8
                nx = x + dx[p]
                ny = y + dy[p]
def move_fish(s_x,s_y):
    for n in range(1,16+1):
        position = find_fish(n)
        if position is None:
            continue
        x,y = position[0],position[1]
        p = m[x][y][1]
        for i in range(8):
            p = (p+i)%8
            nx = x+dx[p]
            ny = y+dy[p]
            if 0<=nx<4 and 0<=ny<4 and not(nx==s_x and ny==s_y):
                m[x][y][0], m[nx][ny][0] = m[nx][ny][0], m[x][y][0]
                m[x][y][1], m[nx][ny][1] = m[nx][ny][1], p
                break
def food_cheat( x, y):  # 상어가 먹을 수 있는 후보 위치 반환
    positions = []
    direction = m[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= m[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions
def dfs(s_x,s_y,eat,total):

    eat+= m[s_x][s_y][0]
    m[s_x][s_y] = [-1, m[s_x][s_y][1]]  #상어 위치는 티만 내주고 굳이 바꿀 필요는 없다
    print('shark')
    print(m)
    move_fish(s_x,s_y)
    print('after move')
    print(m)
    #
    result = food_cheat(s_x, s_y)
    # 해당 먹이 먹는 모든 과정 탐색
    answer = max(eat, total + m[s_x][s_y][0])
    for next_x, next_y in result:
        dfs( next_x, next_y,eat, total + m[s_x][s_y][0])

dfs(0,0,eat,0)
print(eat)

