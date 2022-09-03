# 1이 될때까지
# 최대한 많이 나누기를 추생하면 count가 최소가 될 것
# 내 풀이
n,k = map(int,input().split())
c = 0
while n!=1:
    if n%k == 0:
        n = n/k
        c +=1
    else:
        n = n-1
        c += 1
print(c)

# 나동빈 풀이
n,k = map(int,input().split())
c = 0
while True:
    target = (n//k)*k # -1이 몇번 필요한지 검사
    c +=(n-target)
    n = target
    if n<k:
        break
    c +=1
    n//=k
c += n-1
print(c)