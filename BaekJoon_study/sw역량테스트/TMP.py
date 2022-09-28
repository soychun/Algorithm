n = 4
g = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        g[i][j] = [i,j]
def print_g(g):
    for i in range(n):
        print(g[i])
print_g(g)

g_new = [[0]*n for _ in range(n)]
print('--------')
for i in range(n):
    for j in range(n):
        g_new[i][j]=g[j][3-i]
print_g(g_new)


# 배열 돌리기는 할 수 있지만 나는 zip으로 할 꺼야
original = [[1,2],[3,4],[5,6]]
print(original[::-1])  # 반대로 출력 시켜주는 기술
#   output [[5, 6], [3, 4], [1, 2]]
#zip을 소개하자면
a = [1,2,3]
b = ['a','b','c']
print(list(zip(a,b)))
c = list(zip(a,b))
#   output [(1, 'a'), (2, 'b'), (3, 'c')]
print(c)
d,e = zip(*c)
print(d,e)
print(c)
print('------------')
for i in range(0,4):
    c = list(zip(*c))
    print(c)


original = [[1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]]
new_original = list(map(list,zip(*original)))[::-1]
print_g(new_original)


