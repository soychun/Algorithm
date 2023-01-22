# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하는 방법
# 데이터가 거의 정렬되어 있으면 완전 효율적
# 첫번째 데이터는 정렬되어 있다고 생각하고, 두번째 데이터 부터 정렬을 시작

arr = [7,5,9,0,3,1,6,2,4,8]

# 삽입 방식은? 한칸한칸 비교하며 스와프
# print(3)
# print(2)
for i in range(1,len(arr)):
    for j in range(i,0,-1):  #i-1,-1로 처음에 했는데, 다른 이유 찾아보자
        # print(i,'   ',j)
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else:
            break

print(arr)