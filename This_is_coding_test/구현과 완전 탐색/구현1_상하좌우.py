# 여행자가 nxn 배열에서 상하좌우로 움직이는 문제
# 코테에서 시뮬레이션 유형, 구형 유형, 완전 탐색 유형은 서로 유사한 점이 많다

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n = int(input())
S = list(input().split())
x,y = 1,1
for s in S:
    print(s)
    if s == 'L':
        if y>1:
            x = x+dx[0]
            y = y+dy[0]
    elif s=='R':
        if y<n:
            x = x+dx[1]
            y = y+dy[1]
    elif s=='U':
        if x>1:
            x = x+dx[2]
            y = y+dy[2]
    elif s == 'D':
        if x<n:
            x = x+dx[3]
            y = y+dy[3]
    print(x, y)
print('final : ',x,y)