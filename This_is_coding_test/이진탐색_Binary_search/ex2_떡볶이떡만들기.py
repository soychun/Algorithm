n,m = 4,6
arr = [19,15,10,17]

s = 0
e = max(arr)

result = 0

# mid가 찾는 지점

while s <=e:
    total =0
    mid = (s+e)//2


    for x in arr:
        if x>mid:
            total += x-mid
    print(mid,s,e,total)
    if total <m: #더 잘라야 됨
        e = mid -1
    else:
        result = mid
        s = mid +1

print(result)



