import json

from src.graph.graph import Graph


def load_graph(filepath):

    graph = Graph()

    with open(filepath) as file:

        data = json.load(file)

    for edge in data["roads"]:

        source = edge[0]

        destination = edge[1]

        distance = edge[2]

        graph.add_edge(
            source,
            destination,
            distance
        )

    return graph