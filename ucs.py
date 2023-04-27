from queue import PriorityQueue
from collections import defaultdict

graph = {
    'S':{'A':5, 'B':9, 'D':6},
    'A':{'B':3},
    'B':{'A':2, 'C':1},
    'C':{'S':6, 'F':7},
    'D':{'C':2, 'E':2},
    'E':{'G':7},
    'F':{'D':2, 'G':8},
    'G':{}
}

def ucs(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))

    closed_list = {}

    cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        current_cost, current_node = open_list.get()
 
        closed_list[current_node] = current_cost

        if current_node == goal:
            path = []
            while current_node is not None: 
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]

        for neighbor, neighbor_cost in graph[current_node].items():
            tentative_cost = current_cost + neighbor_cost

            if neighbor in closed_list:
                continue

            if neighbor in cost and tentative_cost >= cost[neighbor]:
                continue

            open_list.put((tentative_cost, neighbor)) 

            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node
            
        print('Open List:', list(open_list.queue))
        print('Closed List:', closed_list)
        print()

    return None

# graph = defaultdict(dict)

# n = int(input("Enter no. of edges : "))
# for i in range(n):
#     u = int(input())
#     v = int(input())
#     c = int(input())
#     graph[u].append({v:c})
# print(graph)

print(dict(graph))
start = input("Enter Start Node : ")
goal = input("Enter Goal Node : ")
print()

path, cost = ucs(start, goal)
print('Path:', path)
print('Cost:', cost)