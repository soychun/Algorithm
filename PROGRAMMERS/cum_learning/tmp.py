arr = [8,4,6,2,9,1,3,7,5,0]

def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    merged_arr =[]
    l=r=0
    while l<len(l_arr) and r<len(r_arr):
        if l_arr[l]<r_arr[r]:
            merged_arr.append(l_arr[l])
            l+=1
        else:
            merged_arr.append(r_arr[r])
            r+=1
    merged_arr+=l_arr[l:]
    merged_arr += r_arr[r:]
    return merged_arr

print(merge_sort(arr))