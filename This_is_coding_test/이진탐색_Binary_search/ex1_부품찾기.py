n = 5
c_list = [8,3,7,9,2]
m = 3
r_list = [5,7,9]

c_list.sort()

이진탐색
def binary_search(arr,target):
    s = 0
    e = len(arr)
    while s<=e:
        mid = (e+s)//2
        if arr[mid]<target:
            s = mid+1
        elif arr[mid]>target:
            e = mid-1
        else:
            return 'yes'
    return 'no'

for x in r_list:

    print(binary_search(c_list,x),end=' ')

# no yes yes

계수 정렬
tmp = {}
for i in c_list:
    tmp[i]=1
for i in r_list:
    if tmp.get(i,0)==1:
        print('yes',end = ' ')
    else:
        print('no',end=' ')

집합
# print(set(c_list)&set(r_list))
c_list=set(c_list)
for i in r_list:
    if c_list&set([i]):
        print('yes')
    else:
        print('no')