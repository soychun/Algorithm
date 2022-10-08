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
    # 시작노드로 가기 위한 최단 경로는  0으로 설정하며, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        # 이미 처리된 적이 있는 노드라면 무시, 현재 가장 짧은 상태라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드에서 처리할껀데, 이거랑 연결되어있는거중에 현재 거리에서 더 짧은게 있는지 검사해서
        for v in g[now]:
            cost = dist + v[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q,(cost,v[0]))
                # 갱신 후 큐에 넣기
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == inf:
        print('inf')
    else:
        print(distance[i])