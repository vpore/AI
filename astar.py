from queue import PriorityQueue

graph = {
    'S': {'1': 3, '4': 4},
    '1': {'2': 4, '4': 5},
    '2': {'1': 4, '5': 5, '3': 4},
    '3': {'2': 4},
    '4': {'S': 4, '1': 5, '5': 2},
    '5': {'4': 2, '2': 5, '6': 4},
    '6': {'5': 4, '7': 3},
    '7': {'6': 3}
}

h = {
    'S': 15, '1': 14, '2': 10, '3': 8, '4': 12, '5': 10, '6': 10, '7': 0
}

def a_star(start, goal):
    open_list = PriorityQueue()
    open_list.put((0+h[start], start, 0))

    closed_list = {}

    cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        curr_f, current_node, current_cost = open_list.get()

        closed_list[current_node] = (current_cost, h[current_node])

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

            open_list.put((tentative_cost+h[neighbor], neighbor, tentative_cost))

            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node

        print('Open List:', list(open_list.queue))
        print('Closed List:', closed_list)
        print()

    return None


start = input("Enter Start Node : ")
goal = input("Enter Goal Node : ")
print()

path, cost = a_star(start, goal)
print('Path:', path)
print('Cost:', cost)