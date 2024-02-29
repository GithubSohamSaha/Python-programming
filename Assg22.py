from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def read_edge_list_file(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                u, v = map(int, line.strip().split())
                self.add_edge(u, v)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def remove_node(self, node):
        del self.graph[node]
        for n in self.graph:
            if node in self.graph[n]:
                self.graph[n].remove(node)

    def print_nodes(self):
        print("Nodes:", list(self.graph.keys()))

    def print_edges(self):
        print("Edges:")
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                print(f"({node}, {neighbor})")

    def degree_distribution(self):
        degrees = [len(neighbors) for neighbors in self.graph.values()]
        return dict((degree, degrees.count(degree)) for degree in set(degrees))

    def clustering_coefficient(self, node):
        neighbors = self.graph[node]
        num_neighbors = len(neighbors)
        if num_neighbors < 2:
            return 0.0
        total_triangles = sum(len(set(self.graph[neighbor]).intersection(neighbors)) for neighbor in neighbors)
        return 2.0 * total_triangles / (num_neighbors * (num_neighbors - 1))

    def connected_components(self):
        visited = set()
        components = []
        for node in self.graph:
            if node not in visited:
                component = self.bfs(node)
                visited.update(component)
                components.append(component)
        return components

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
        return visited

    def single_source_shortest_paths(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        return distances

# Example usage:
graph = Graph()
graph.read_edge_list_file("edge_list.txt")

print("Nodes and Edges:")
graph.print_nodes()
graph.print_edges()

print("\nDegree Distribution:")
print(graph.degree_distribution())

print("\nClustering Coefficient of Node 1:")
print(graph.clustering_coefficient(1))

print("\nConnected Components:")
components = graph.connected_components()
for i, component in enumerate(components, start=1):
    print(f"Component {i}: {list(component)}")

print("\nSingle Source Shortest Paths from Node 1:")
shortest_paths = graph.single_source_shortest_paths(1)
print(shortest_paths)
