# g = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
g = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}
# def dfs(g,n_s):
#     s = [n_s]   #node start
#     visited = [0]*(len(g)+1)
#     answer = [n_s]
#     while s:
#         n_c = s.pop()  #node current
#         visited[n_c] = 1
#         answer.append(n_c)
#         for n_f in g[n_c]:
#             if visited[n_f]==0:
#                 s.append(n_f)
#     return answer[1:]
# print(dfs(g,1))

from collections import deque
def bfs(g,n_s):
    s = deque([n_s])
    v = [0]*(len(g)+1)
    answer = []
    while s:
        n_c = s.popleft()
        answer.append(n_c)
        v[n_c] = 1
        for n_f in g[n_c]:
            if v[n_f]==0:
                s.append(n_f)
    return answer
print(bfs(g,1))