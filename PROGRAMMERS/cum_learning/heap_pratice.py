from heapq import heapify
import heapq
# 최소 힙, 파이썬은 기본이 최소 힙이다.
heap_p = []
heapq.heappush(heap_p,4)
heapq.heappush(heap_p,7)
heapq.heappush(heap_p,1)
heapq.heappush(heap_p,3)
print(heap_p)
heapq.heappop(heap_p)
print(heap_p)

max_heap = []
# 최대 힙
heapq.heappush(max_heap,(-4,4))
heapq.heappush(max_heap,(-7,7))
heapq.heappush(max_heap,(-1,1))
heapq.heappush(max_heap,(-3,3))
print(max_heap)
heapq.heappop(max_heap)
print(max_heap)

side_heap = []
heapq.heappush(side_heap,(4,-4))
heapq.heappush(side_heap,(7,-7))
heapq.heappush(side_heap,(1,-1))
heapq.heappush(side_heap,(3,-3))
for i in range(len(side_heap)):
    print(heapq.heappop(side_heap))

