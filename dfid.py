from collections import defaultdict

# list representation

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DLS(self, src, target, maxDepth, open, close, path):
		open.append(src)
		if src == target:
			return True
		
		if maxDepth <= 0:
			return False
		
		print("Open List : ", open)
		print("Close List : ", close)
		print()

		open.pop()
		close.append(src)

		for i in self.graph[src]:
			result = self.DLS(i, target, maxDepth-1, open, close, path)
			if (result):
				path.append(i)
				return True
		return False

	def IDDFS(self, src, target, maxDepth):
		print('Graph : ', dict(self.graph))
		print()
		
		for i in range(maxDepth):
			open = []
			close = []
			path = []
			print("Max Depth : ", i)

			res = self.DLS(src, target, i, open, close, path)

			print("Open List : ", open)
			print("Close List : ", close)
			print()

			if (res):
				path.append(src)
				path.reverse()
				print(path)
				return True
		return False


# Create a graph given in the above diagram
n = int(input("Enter no. of edges : "))
g = Graph(n)

for i in range(n):
	print("\nEnter edge ", i+1, " -")
	u = int(input("Enter u : "))
	v = int(input("Enter v : "))
	g.addEdge(u, v)

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(2, 6)

src = int(input("\nEnter source node : "))
target = int(input("Enter target node : "))
maxDepth = int(input("Enter maximum depth : "))
print()

if g.IDDFS(src, target, maxDepth) == True:
	print("Target is reachable from source " +
            "within max depth")
else:
	print("Target is NOT reachable from source " +
            "within max depth")
