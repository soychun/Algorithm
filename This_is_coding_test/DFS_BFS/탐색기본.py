# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다
# 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다

# 스텍 자료구조와 큐 자료구조
# from collections import deque

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



# 재귀함수를 문제풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다
# 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다
