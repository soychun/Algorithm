n = 10
k =24
# B 두번만
# K번째 문자열의 두 번째 B의 위치를 구하기오
# P의 이진수\
#
bag =  []
for i in range(n):
    bag.append(i+1)
print(bag)
print(len(bag))
# 순열 경우의 수를 고려한 다음, 24번째ㅐ

seq_list = []
v = [0]*len(bag)
s = []
def dfs(L,B):
    if L==2:
        seq_list.append(list(map(int,s)))
        print(' '.join(map(str,s)))
    else:
        for i in range(B,len(bag)):
            s.append(bag[i])
            dfs(L+1,i+1)
            s.pop()

dfs(0,0)
print(seq_list)
a = sorted(seq_list,reverse=True)
print(sorted(a[k-1])[1])