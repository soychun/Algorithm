arr = [3,5,2,6,3,3,1,0,6,9]
# 딕셔너리를 활용한 방법
# 리스트를 활용한 방법도 있지만 비효율적이라 이렇게만 써 둔다
tmp = {}
for x in range(len(arr)):
    tmp[arr[x]] = tmp.get(arr[x],0)+1
print(tmp)
result=[]
for i in range(min(arr),max(arr)+1):
    while i in tmp and tmp[i]!=0:
        result.append(i)
        tmp[i]-=1
print(result)

