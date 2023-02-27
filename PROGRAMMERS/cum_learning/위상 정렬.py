# 위상 정렬의 특징
# 위상 정렬은 사이클이 없는 방향 그래프 (DAG)에 대해서만 수행할 수 있다.
# ※ DAG (Direct Acyclic Graph) : 순환하지 않는(=사이클이 없는) 방향 그래프
#
# 위상 정렬에서는 여러 가지 답이 존재할 수 있다. 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 가지 답이 존재할 수 있다는 의미이다.
#
# 모든 원소를 방문하기 전에 큐가 비게 된다면 사이클이 존재한다고 판단할 수 있다. 왜냐하면 사이클에 포함된 원소 중에서 해당되는 어떠한 원소도 큐에 들어가지 못하게 되기 때문이다.
#
# 보통 큐로 구현하나, 스택을 이용한 DFS를 이용해 위상 정렬을 구현할 수도 있다.


# 입력 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
#
# 출력 예시
# 1 2 5 3 6 4 7
import time
start = time.time()
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
g = dict()
enter = [0]*(n+1)
enter[0]=-1
for i in range(n):
    g[i+1]=[]
for i in range(m):
    n_,v_ = map(int,input().split())
    g[n_]=g.get(n_,[])+[v_]
    enter[v_]+=1
# print(g)
# print(enter)
from collections import deque
q = deque()
# print(enter[1:].index(0)+1)
q.append(enter[1:].index(0)+1)
enter[enter[1:].index(0)+1]=-1
# print(enter)
# print(q)

# 내 첫번째 풀이
while q:
    # print(q)
    n_c = q.popleft()
    print(n_c,end = ' ')
    # print('n_c : ',n_c,g)
    tmp = g[n_c]
    g[n_c]=[]  #그래프 제거

    for n_f in tmp:
        enter[n_f]-=1 #진입 차수 줄이기

    for i in range(1,len(enter)):
        if enter[i]==0:
            q.append(i)
            enter[i]=-1
    # print('end')


# 내 두번째 풀이
while q:
    n_c = q.popleft()
    print(n_c,end = ' ')
    tmp = g[n_c]
# 그래프 제거 부분 뺀다(어차피 그냥 안가면 될 것)
    for n_f in tmp:   # 다 돌면서 진입 차수 줄일 필요는 없다
        enter[n_f]-=1 #진입 차수 줄이기
        if enter[n_f]==0:
            q.append(n_f)
            enter[n_f]=-1

print(time.time()-start)



'''
# 이건 이코테 풀이
import sys
from collections import deque
input = sys.stdin.readline
# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


# 위상 정렬 함수
result = []
q = deque()

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now,end=' ')
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for g in graph[now]:
        indegree[g] -= 1
        if indegree[g] == 0:
            q.append(g)

print(time.time()-start)
'''