"""
             5
           /   \
          3     7
         / \    /
        2   4  8
"""

# Stack

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': [],
    '8': []
}

visited = []
stack = []

def dfs(visited, graph, node, goal):
    if (node not in visited) and (goal not in visited):
        print(node, end = " ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, goal)
print(f"DFS")
dfs(visited, graph, '5' , '4')

# print("\n")
# def output_graph(graph):
#     for node in graph:
#         print(node, ":", graph[node])
# output_graph(graph)