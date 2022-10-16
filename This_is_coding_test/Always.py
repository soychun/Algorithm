# list에서 요소 개수 세기
x = [1,2,3,4,5,5]
print(x.count(5))
# output : 2

# list에서 중복 제거하기
x = [1,2,3,4,5,5]
x_list = list(set(sorted(x)))
# output : [1, 2, 3, 4, 5]

# 숫자를 문자로 생각해서 탐색해서 풀 수도 있다는 것을 명심하자

# list에서 알파벳이 있는지 알아보는 방법
data = ['a','b','1','A']
for x in data:
    print(x,x.isalpha())
#output
    # a
    # True
    # b
    # True
    # 1
    # False
    # A
    # True

# list를 숫자로 바꾸는 방법
a = ['a','b','c']
b = ''.join(a)   #''안엔 구분자, 마음껏 바꿔도 됨
print(a)  # ['a', 'b', 'c']
print(b)  # abc


# 파이썬의 기본 재귀 깊이 제한 1000
# 재귀 최대 깊이 설정
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# sort
a = [(2,1,3),(1,3,3),(3,3,4),(1,1,3)]
print(sorted(a,key=lambda x: (-x[2],-x[0],-x[1])))   # [(3, 3, 4), (2, 1, 3), (1, 3, 3), (1, 1, 3)]
# 첫번째 인자를 기분으로 내림차순 (-), 두번째 인자를 기준으로 내림차순,.,,
print(sorted(a))                                    #[(1, 1, 3), (1, 3, 3), (2, 1, 3), (3, 3, 4)]
print(sorted(a,reverse=True))                       #[(3, 3, 4), (2, 1, 3), (1, 3, 3), (1, 1, 3)]
print(sorted(a,key=lambda  x:(x[2],x[0],x[1])))



remove_set = {0}
a =[i for i in a if i not in remove_set]
# set에 있는 수를 모두 제거하는 방법

# zip


# 순열은 ch[]가 필요하고, 조합은 ch[]가 필요 없지만 BeginWith변수가 꼭 필요하다
# 부분집합의 경우에는 상태트리를 만들어서 선택하는 경우와 선택하지 않는 경우가 필요한 것 같다


# 조합 _ 삼성용
from collections import deque
s = deque()
n = 4
r = 3
def do_somthing(s):
    print(s)
def dfs_notfor(s,L,D):
    if len(s)==r:
        do_somthing(s)
        return
    elif D==n:
        return
    s.append(D+1)
    dfs_notfor(s,L+1,D+1)
    s.pop()
    dfs_notfor(s,L+1,D+1)
dfs_notfor(s,0,0)


# 최댓값은 엄청나게 작게, 최솟값은 엄청나게 크게 하는 방법을 항상 생각하자


a - b 를 구현한 코드입니다.
a_sub_b = [x for x in a if x not in b]


f-string
answer = 7
print(f"정답은 {answer}입니다")

람다표현식
print((lambda a,b:a+b)(3,7))

map함수
map(function, iterable)  iterable이라는 뜻은 반복 가능한 자료형인 리스트나 튜플