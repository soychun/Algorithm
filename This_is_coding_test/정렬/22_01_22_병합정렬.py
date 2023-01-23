arr = [8,4,6,2,9,1,3,7,5,0]

def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2   #반을 나눠서 중간을 자른다
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    print('div',l_arr+r_arr)
    merged_arr = []
    l=r = 0
    while l<len(l_arr) and r<len(r_arr):
        if l_arr[l]<r_arr[r]:
            merged_arr.append(l_arr[l])
            l+=1
        else:
            merged_arr.append(r_arr[r])
            r+=1
    # print('before',merged_arr)
    merged_arr +=l_arr[l:]   #나머지를 정렬하지도 않고 붙일 수 있는 이유는 앞에서 이미 정렬했기 때문이다.
    merged_arr +=r_arr[r:]    # l이 먼저든 r이 먼저든 상관 없다. 
    print(merged_arr)
    return merged_arr

arr = merge_sort(arr)
print(arr)