# 순차탐색 : for문으로 돌면서 문자열이 같다면 return하는 방식

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요')

# 5 Dongbin

input_data = input().split()
print(input_data)
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
arr = input().split()
# Hanul Jonggu Dongbin Taeil Sangwook


def sequential_search(n,target,arr):
    for i in range(n):
        if arr[i]==target:
            return i
print(arr[sequential_search(n,target,arr)])