import heapq
from sys import stdin
input = stdin.readline
inf = int(1e9)
v,e = map(int,input().split())
g = [[] for _ in range(v+1)]
distance = [inf]*(v+1)

start = int(input())
for _ in range(e):
    u,v,w = map(int,input().split())
    g[u].append((v,w))
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in g[now]:
            cost = dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(start)
for i in range(1,len(distance)):
    if distance[i]==inf:
        print('INF')
    else:print(distance[i])


