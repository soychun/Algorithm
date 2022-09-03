# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면됨
# 완전 탐색 (brute forcing) 문제 유형이라고 불림
n = int(input())
s =0
b = 0
c = 0
result = 0
while True:
    while True:
        while True:
            print('%02d:%02d:%02d' %(s,b,c))
            if (s % 10 == 3 or s // 10 == 3 or b % 10 == 3 or b // 10 == 3 or c % 10 == 3 or c // 10 == 3):
                result += 1
            if c==59:
                c=0
                break
            else:

                c+=1
        if b==59:
            b=0
            break
        else:
            b+=1
    if s==5:
        break
    else:
        s+=1
print(result)



# 나동빈 풀이
h = int(input())
count =0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)