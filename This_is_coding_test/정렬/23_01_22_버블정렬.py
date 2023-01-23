arr = [9,8,7,6,5,4,3,2,1,0]

# 첫번째 시도였으나 한번만하는 정렬은 젤 큰 숫자만 뒤로 보낼 뿐이다.
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1):
#
#         if arr[i] >arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#         else:
#             pass
#     print(i,arr)
# print(arr)

# 2차시도
for i in range(len(arr)-1,0,-1):
    for j in range(i):

        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
            pass
    print(i, arr)
print(arr)

# 간단한 코드 구글링 해서 붙여넣기 (아직내꺼아님
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)