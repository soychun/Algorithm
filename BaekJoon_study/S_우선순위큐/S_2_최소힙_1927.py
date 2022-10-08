import heapq
from sys import stdin
input = stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x>0:
        heapq.heappush(q,x)
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))

