arr = [8,4,6,2,5,1,3,7,9,0]

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = len(arr)//2   #이걸 뭘로 하던 상관 없는 듯?

    l_arr,p_arr,r_arr = [],[],[]

    for v in arr:
        if v<arr[pivot]:
            l_arr.append(v)
        elif v>arr[pivot]:
            r_arr.append(v)
        else:
            p_arr.append(v)

    print(l_arr,p_arr,r_arr)

    return quick_sort(l_arr)+quick_sort(p_arr)+quick_sort(r_arr)

print('before : ',arr)
arr = quick_sort(arr)
print('after : ',arr)