import heapq
inf = int(1e9)
n,m,c = map(int,input().split())
g = [[] for i in range(n+1)]
distance = [inf]*(n+1)
for i in range(m):
    a,b,c = map(int,input().split())
    g[a].append((b,c))

def dijkstra(c)