# n,m = map(int,input().split())
# lab = []
# for i in range(n):
#     lab.append(list(map(int, input().split())))
#
# stat = [[0]*(n) for _ in range(n)]
# locat = []
# for i in range(n):
#     for j in range(n):
#         if lab[i][j] == 1:
#             stat[i][j]='-'
#         elif lab[i][j]==0:
#             stat[i][j] = '+'
#         elif lab[i][j]==2:
#             locat.append((i,j))
# print(lab)
# print(stat)
# print(locat)

n = 7
m = 2
lab = []
locat = [(0, 0), (0, 2), (3, 0), (3, 6), (6, 0), (6, 4), (6, 6)]  #조합으로 n 만큼 뽑기
stat = [['0', '+', '0', '+', '-', '-', '+'], ['+', '+', '-', '+', '-', '+', '+'], ['+', '-', '-', '-', '-', '+', '+'], ['0', '-', '+', '+', '+', '+', '0'], ['-', '+', '+', '+', '+', '-', '-'], ['+', '-', '+', '+', '+', '+', '+'], ['0', '-', '+', '+', '0', '+', '0']]
bag_act = [0,1]
bag_dea = [2,3,4,5,6]
for i in bag_dea:
    stat[locat[i][0]][locat[i][1]] = '*'

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
while True:
    print('cnt',cnt)
    for i in range(n):
        print(stat[i])
    for i in range(n):
        for j in range(n):
            if stat[i][j] == str(cnt):
                for k in range(4):

                    ni = i+dx[k]
                    nj = j+dy[k]
                    if 0<=ni<n and 0<=nj<n and stat[ni][nj]!='-' and stat[ni][nj]!='*' and stat[ni][nj]=='+':
                        stat[ni][nj] = str(cnt+1)
    cnt += 1
    print('final')
    cnt_e = 0
    for i in range(n):
        cnt_e += stat[i].count('+')
    print(cnt_e)
    for i in range(n):
        print(stat[i])