# 모험가가 N명 있음. 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다
# 길드장은 모험가 그룹을 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 됨
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라
'''
N : 5
input : 2 3 1 2 2
output : 2 그룹1에 1,2,3 그룹 2에 2,2
추가 : 몇 명의 모험가는 마을에 그대로 남아 있어도 괜찮다
'''

n = int(input())
x = list(map(int,input().split()))
x_list = list(set(sorted(x)))

result = 0

for i in x_list:
    # print(i)
    if i <= x.count(i):
        result+=x.count(i)//i

print(result)





# 5
# 1 1 4 5 2

# 6
# 1 4 4 2 2 1


# 나동빈풀이
# 앞에서부터 공포도를 하나씩 확인해 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도 보다 크거나 갔다면 바로 그룹 결성해서 보내버리는
# 방법을 제시한다.

n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
count = 0
for i in data:
    count+=1
    if count>=i:
        result+=1
        count = 0
print(result)