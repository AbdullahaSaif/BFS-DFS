"""
             5
           /   \
          3     7
         / \    /
        2   4  8
"""

# Quee

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'F': ['H']
}

visited = []
queue = []

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print(f"BFS")
bfs(visited, graph, 'A', 'H')

# print("\n")
# def output_graph(graph):
#     for node in graph:
#         print(node, ":", graph[node])
# output_graph(graph)