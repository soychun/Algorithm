# 배열 내부의 데이터가 정렬되어 있다면 아주 유용한 알고리즘
# 탐색 범위가 1000만을 넘어가면 접근해 볼 것 (logN이 필요.)
# input() 보다는 sys.stdin.readline()

# 1000억 이상 ? 무조건 이빈 탐색

# O(log N)

n,target = list(map(int,input().split()))
arr = list(map(int, input().split()))

# 10 4
# 0 2 4 6 8 10 12 14 16 18

print(len(arr))

s =0
e = n-1
index = 0
def binary_search(arr, target,s,e):
    while s<=e: # 원래 while True로 했는데 생각해보니까 배열 안에 없을 경우 빠져 나오는 것도 필요하다
        mid = (s + e)//2
        if arr[mid]>target:
            e = mid-1
        elif arr[mid]<target:
            s = mid+1
        else:
            return mid
    return None
print(binary_search(arr,target,0,n-1))