import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

import networkx as nx
import matplotlib.pyplot as plt

def draw_shortest_path(
        graph,
        shortest_path,
        output_path
):

    G = nx.Graph()

    for node in graph.graph:

        for neighbor, weight in graph.graph[node]:

            G.add_edge(
                node,
                neighbor,
                weight=weight
            )

    pos = nx.spring_layout(
        G,
        seed=42
    )

    plt.figure(
        figsize=(12, 8)
    )

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=3000
    )

    nx.draw_networkx_labels(
        G,
        pos
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=1
    )

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    path_edges = []

    for i in range(
        len(shortest_path) - 1
    ):

        path_edges.append(
            (
                shortest_path[i],
                shortest_path[i + 1]
            )
        )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        width=5
    )

    plt.title(
        "Optimized Route"
    )

    plt.axis("off")

    plt.savefig(
        output_path,
        bbox_inches="tight"
    )

    plt.close()