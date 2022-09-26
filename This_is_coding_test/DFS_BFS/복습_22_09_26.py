# 조합 기본 (for문 사용)

n = 4
r = 2
s = []
def dfs(L,B):
    if L == r:
        print(s)
    else:
        for i in range(B,n):
            s.append(i+1)
            dfs(L+1,i+1)
            s.pop()
dfs(0,0)

# 삼성DFS를 이용한 조합 구현
# 조합+DFS 알고리즘은 00 중 M개를 골랐을 때 최소(최대)가 되는 값을 찾으세요 (순서가 없는 경우)
# 와 같은 형식의 문제가 있을 때 사용 가능하다
# 보통 재귀함수를 이용


# 조합 응용 (for문 안사용)  : 내일도 복습할 것
# https://kimjingo.tistory.com/205
from collections import deque
s = deque()
n = 4
r = 3
def do_somthing(s):
    print(s)
def dfs_notfor(s,D):
    if len(s)==r:
        do_somthing(s)
        return
    elif D==n:
        return
    s.append(D+1)
    dfs_notfor(s,D+1)
    s.pop()
    dfs_notfor(s,D+1)
dfs_notfor(s,0,0)