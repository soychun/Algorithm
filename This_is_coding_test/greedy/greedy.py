# 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유
# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로
# 작은 단위의 동전들을 종합해 다른 해가 나올 수 없다.

# 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다.
'''
동전 문제
N = 1260
s = [500,100,50,10]
n = 0
for i in s:

    n = n+ N//i
    N = N%i
print(n)
'''
'''
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
'''

# 곱하기 혹은 더하기
S = input()
result = 0
for s in S:
    # print(s)
    s = int(s)
    if(s==0 or s==1 or result==0 or result==1):
        result = result + s
        # print('if')
    else:
        result = result * s
        # print('else')
print(result)
