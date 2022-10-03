리스트 맵 리스트 집

zip은 서로 다른 배열을 하나씩 묶어주는 메소드이다
zip이 아니라, 사실 zip(*)을 이용한 unzip을 다시 리스트로 묶어줌으로써 해체 후 재합성
그 다음에 reverse를 [::-1]

def print_g(g):
    for i in range(len(g)):
        print(g[i])
array_original = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

# 시계방향:
#             1 2 3         7 4 1                   |1| 2 3        [7 4 1]
#             4 5 6    ->   8 5 2   reverse sort,   |4| 5 6    ->   8 5 2
#             7 8 9         9 6 3     unzip         |7| 8 9         9 6 3

print(array_original)
print_g(array_original)

for i in range(4):
    array_original = list(map(list, zip(*array_original[::-1])))
    print(array_original)
    print_g(array_original)

            # output
            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # [1, 2, 3]
            # [4, 5, 6]
            # [7, 8, 9]
            # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            # [7, 4, 1]
            # [8, 5, 2]
            # [9, 6, 3]
            # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
            # [9, 8, 7]
            # [6, 5, 4]
            # [3, 2, 1]
            # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
            # [3, 6, 9]
            # [2, 5, 8]
            # [1, 4, 7]
            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # [1, 2, 3]
            # [4, 5, 6]
            # [7, 8, 9]

print('------------')

array_original = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

# 시계 반대방향:
#             1 2 3         3 6 9                   1 2 |3|        [3 6 9]
#             4 5 6    ->   2 5 8      unzip,       4 5 |6|    ->   2 5 8
#             7 8 9         1 4 7     reverse sort  7 8 |9|         1 4 7

print(array_original)
print_g(array_original)

for i in range(4):
    array_original = list(map(list, zip(*array_original)))[::-1]
    print(array_original)
    print_g(array_original)

            # output
            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # [1, 2, 3]
            # [4, 5, 6]
            # [7, 8, 9]
            # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
            # [3, 6, 9]
            # [2, 5, 8]
            # [1, 4, 7]
            # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
            # [9, 8, 7]
            # [6, 5, 4]
            # [3, 2, 1]
            # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            # [7, 4, 1]
            # [8, 5, 2]
            # [9, 6, 3]
            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # [1, 2, 3]
            # [4, 5, 6]
            # [7, 8, 9]
