class NavigationGraph:
    graph: dict = {}
    
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.graph and to_node in self.graph:
            self.graph[from_node].append(to_node)

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def __str__(self):
        return str(self.graph)