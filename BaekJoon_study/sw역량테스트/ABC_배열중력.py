array_original = [[0,1,1,1,0],
                  [2,0,1,1,0],
                  [0,1,0,2,0],
                  [1,0,0,1,0],
                  [0,2,1,1,0],
                  [0,0,0,1,1]]        # 1 이 블럭, 0이 반공간, 2가 벽

n = 6
m = 5

for i in range(n-1,-1,-1):
    print(i)
    for j in range(m):
        if array_original[i][j] == 1 : #공이면
            r = i
            while True:
                if 0<=r+1<n and array_original[r + 1][j]==0:
                    array_original[r+1][j],array_original[r][j] = array_original[r][j],array_original[r+1][j]
                    r = r+1

                else:
                    break

def print_g(g):
    for i in range(len(g)):
        print(g[i])

print_g(array_original)


# [0, 0, 0, 1, 0]
# [2, 0, 0, 1, 0]
# [0, 1, 0, 2, 0]
# [0, 1, 1, 1, 0]
# [0, 2, 1, 1, 0]
# [1, 0, 1, 1, 1]