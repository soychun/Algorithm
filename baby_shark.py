arr = [1,2,3,4,5]
print(arr)
def gen_combi(arr,n):
    result = []
    if n == 0 :
        return[[]]

    for i in range(0,len(arr)):
        ele = arr[i]
        rest_arr = arr[i+1:]
        for C in gen_combi(rest_arr,n-1):
            result.append([ele]+C)
    return result
def get_per(arr,n):
    result = []
    if n==0:
        return[[]]
    for i, ele in enumerate(arr):
        for P in get_per(arr[:i]+arr[i+1:],n-1):
            result.append([ele]+P)
    return result
print(get_per(arr,2))
print(len(get_per(arr,2)))
print(gen_combi(arr,2))
print(len(gen_combi(arr,2)))