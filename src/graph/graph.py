class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(
        self,
        source,
        destination,
        distance,
        bidirectional=True
    ):

        self.graph.setdefault(source, [])
        self.graph.setdefault(destination, [])

        self.graph[source].append(
            (destination, distance)
        )

        if bidirectional:

            self.graph[destination].append(
                (source, distance)
            )

    def get_neighbors(self, node):

        return self.graph.get(node, [])

    def get_nodes(self):

        return list(self.graph.keys())

    def display(self):

        for node, neighbors in self.graph.items():

            print(
                f"{node} -> {neighbors}"
            )