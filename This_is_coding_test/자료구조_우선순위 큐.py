# 데이터를 우선순위에 따라 처리하고 싶을 때 사용  / 들어간 순서에 상관 없이
#     예시 ) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우
# 구현방법 : 1. 리스트를 이용한 탐색 2. 힙 자료구조를 이용 (heap)
#
# 힙의 특징
# -완전이진트리자료구조
# -항상 루트노드를 제거한다
#     최소 힙 : 루트노드가 가장 작은 값을 가짐 (가장 작은 값부터 제거)
#     최대 힙 : 루트노드가 가장 큰 값을 가짐   (가장 큰 값부터 제거)

# 힙에 원소를 넣을 때, 힙에서 원소를 꺼낼 때 모두 heapify를 수행한다


import heapq     #파이썬은 기본적으로 minheap


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,value)
    print(h)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)

for i in range(n):
    print(res[i])


from heapq import heapify
import heapq
heap_p = []
heapq.heappush(heap_p,4)
heapq.heappush(heap_p,7)
heapq.heappush(heap_p,1)
heapq.heappush(heap_p,3)
# heapq.heappush(heap_p,4)
# heapq.heappush(heap_p,3)
# heapq.heappush(heap_p,1)
# heapq.heappush(heap_p,2)
# heapq.heappush(heap_p,5)
# heapq.heappush(heap_p,6)
print(heap_p)
for i in range(len(heap_p)):
    result = heapq.heappop(heap_p)
    print(result)

print('---------------')
# heap = [4,3,1,2,5,6]
heap = [4,7,1,3]
heapify(heap)
print(heap)

for i in range(len(heap)):
    result = heapq.heappop(heap)
    print(result)