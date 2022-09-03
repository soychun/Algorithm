# abstract data structure
# 자료구조의 방법이 코드로 정의된 것이 아니라, 그 구조의 행동 양식만 정의된 것.

# 탐색 (search) : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
#  - 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸.
#  - 대표 : DFS, BFS
#
# 자료 구조란 데이터를 표현하고 관리하고 처리하기 위한 구조
# - push (삽입)
# - pop (삭제)
# + 고려 사항 : 오버플로, 언더플로
#
# stack : 선입후출
# 보통 list로 구현하는 듯.

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack) #최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력


# queue : 선입선출
# 보통 from collections import deque

from collections import deque
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
# 리스트로 변경하고자 하면, list(queue)
