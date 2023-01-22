# 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸고,
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 방법

# 데이터의 개수가 많아지면 굉장히 비효율적

arr = [7,5,9,0,3,1,6,2,4,8]

# 처음 작성한 코드. if else 필요가 없다.
# print(min(arr))
# print(arr.index(min(arr)))
# for i in range(len(arr)):
#     if arr[i]==min(arr):
#         pass
#     else:
#         tmp =arr.index(min(arr[i:]))   #앞에다 몰아놓고 그건 이제 신경 안쓴다.
#         # print(i,'',arr.index(min(arr)))
#         arr[i],arr[tmp] = arr[tmp],arr[i]
#         # print(arr)
# print(arr)

# 두번째 작성한 코드. if else 필요 없음 반영. 필요 없는 이유는
# for i in range(len(arr)):
#
#     tmp =arr.index(min(arr[i:]))   #앞에다 몰아놓고 그건 이제 신경 안쓴다.
#     # print(i,'',arr.index(min(arr)))
#     arr[i],arr[tmp] = arr[tmp],arr[i]
#     # print(arr)
# print(arr)

# 생각해보니 if else 쓴 이유 중복되는 숫자가 있을 경우 처리하기 위해서?
# 위에 예시에는 중복이 없다.
# 어떻게 해야할 지 모르겠음
arr = [7,5,9,0,3,1,6,2,4,8,5]


