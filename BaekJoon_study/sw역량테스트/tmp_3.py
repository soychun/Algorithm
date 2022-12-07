# graph = {
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

graph = {
    1: [2, 3, 4],
    2: [1,4],
    3: [1,4],
    4: [1,2,3]
}
def dfs_stack(adjacent_graph, start_node):
	stack = [start_node]
	visited = []

	while stack:
		current_node = stack.pop()
		if current_node not in visited:
			visited.append(current_node)
		for adjacent_node in sorted(adjacent_graph[current_node],reverse=True):
			if adjacent_node not in visited:
				stack.append(adjacent_node)
	return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!