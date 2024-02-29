from collections import defaultdict, deque
from Assg22 import Graph
class DiGraph(Graph):
    def __init__(self):
        super().__init__()

    def predecessors(self, node):
        preds = []
        for n, neighbors in self.graph.items():
            if node in neighbors:
                preds.append(n)
        return preds

    def successors(self, node):
        return self.graph[node]

    def reverse_edges(self):
        reversed_graph = defaultdict(list)
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                reversed_graph[neighbor].append(node)
        self.graph = reversed_graph

    def kosaraju(self):
        def dfs(node, visited, stack):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, stack)
            stack.append(node)
        def reverse_graph():
            reversed_graph = defaultdict(list)
            for node, neighbors in self.graph.items():
                for neighbor in neighbors:
                    reversed_graph[neighbor].append(node)
            return reversed_graph
        def dfs_scc(node, visited, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_scc(neighbor, visited, component)
        visited = set()
        stack = []
        # Step 1: Perform DFS and fill the stack based on finishing times
        for node in self.graph:
            if node not in visited:
                dfs(node, visited, stack)
        # Step 2: Reverse the graph
        reversed_graph = reverse_graph()
        # Step 3: Perform DFS on reversed graph in stack order
        visited.clear()
        scc_list = []
        while stack:
            node = stack.pop()
            if node not in visited:
                component = []
                dfs_scc(node, visited, component)
                scc_list.append(component)
        return scc_list
# Example usage:
digraph = DiGraph()
digraph.read_edge_list_file("edge_list_directed.txt")
print("Predecessors of Node 2:")
print(digraph.predecessors(2))
print("\nSuccessors of Node 2:")
print(digraph.successors(2))
print("\nReversed Edges:")
digraph.reverse_edges()
digraph.print_edges()
print("\nStrongly Connected Components:")
scc = digraph.kosaraju()
for i, component in enumerate(scc, start=1):
    print(f"Component {i}: {component}")
