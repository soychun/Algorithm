import heapq
inf = int(1e9)
n,m = map(int,input().split())
start = int(input())
g = [[]for i in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    g[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v in g[now]:
            cost = dist + v[1]
            if cost<distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q,(cost,v[0]))
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == inf:
        print('inf')
    else:
        print(distance[i])