from collections import defaultdict
visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# graph = {
#     '5': ['3', '7'],
#     '3': ['2', '4'],
#     '7': ['8'],
#     '2': [],
#     '4': ['8'],
#     '8': []
# }

graph = defaultdict(list)
n = int(input("Enter no. of edges : "))
for i in range(n):
    u = int(input())
    v = int(input())
    graph[u].append(v)

print('Graph : ', dict(graph))
start = int(input("Enter start node : "))
print()
print("Following is the Depth-First Search")
dfs(visited, graph, start)